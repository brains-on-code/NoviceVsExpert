import os
import mne
import re
import dask.dataframe as dd
import numpy as np
import pandas as pd
import json
import copy
import sys
from pathlib import Path

mne.set_log_level("WARNING")


def load_raw(participant_number, cores=12, digits=2, scaling_factor=7e-9, logging=True, bandpass=(0.5, 80),
             notch=(50, 100)):
    # setup output for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, 'w')

    print("(01/12) Construct Paths", file=output, flush=True)
    # setup paths for loading
    participant_folder = "./rawData/Participant" + str(participant_number).zfill(digits) + "/"
    eye_tracking_path = participant_folder + "experiment_data.csv"
    eeg_path = participant_folder
    psychopy_csv_path = participant_folder
    psychopy_log_path = participant_folder

    # get path for psychopy log and csv data
    for (dirpath, dirnames, filenames) in os.walk(psychopy_csv_path):
        for file in filenames:
            file, ext = os.path.splitext(file)
            if ext == ".csv" and "test" in file:
                psychopy_csv_path += file + ext
            if ext == ".log":
                psychopy_log_path += file + ext

    # get path for psychopy eeg data
    for (dirpath, dirnames, filenames) in os.walk(participant_folder):
        for file in filenames:
            _file, ext = os.path.splitext(file)
            if ext == ".fif":
                eeg_path += file

    print("(02/12) Read Eye Tracker Data", file=output, flush=True)
    # read tracker data
    df_eye_tracking = pd.read_csv(eye_tracking_path, header=None, sep=";")

    # setup regex for number eextraction
    three_extractor_compiled = re.compile("\((.*), (.*), (.*)\)")
    two_extractor_compiled = re.compile("\((.*), (.*)\)")

    # function to extract numbers from a (x,x,x) format
    def three_extractor(value):
        pattern = three_extractor_compiled.match(value)
        return float(pattern.group(1)), float(pattern.group(2)), float(pattern.group(3))

    # function to extract numbers from a (x,x) format
    def two_extractor(value):
        pattern = two_extractor_compiled.match(value)
        return float(pattern.group(1)), float(pattern.group(2))

    # get type for parallel processing
    meta_type = dd.utils.make_meta(0.0)

    # partition dataframe for parallel work
    ddf_eye_tracking = dd.from_pandas(df_eye_tracking, npartitions=cores)

    print("(03/12) Transform Eye Tracker Data", file=output, flush=True)
    # extract the data from the eye-tracking csv to numbers and rename the columns
    df_0 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[0]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["l_gaze_point_in_user_coordinate_system_x", "l_gaze_point_in_user_coordinate_system_y",
                 "l_gaze_point_in_user_coordinate_system_z", ],
    )
    df_1 = pd.DataFrame(ddf_eye_tracking[1].compute().transpose().tolist(), columns=["l_valid"])
    df_2 = pd.DataFrame(ddf_eye_tracking[2].compute().transpose().tolist(), columns=["r_valid"])
    df_3 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[3]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["r_gaze_point_in_user_coordinate_system_x", "r_gaze_point_in_user_coordinate_system_y",
                 "r_gaze_point_in_user_coordinate_system_z", ],
    )
    df_4 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[4]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["l_gaze_origin_in_user_coordinate_system_x", "l_gaze_origin_in_user_coordinate_system_y",
                 "l_gaze_origin_in_user_coordinate_system_z", ],
    )
    df_5 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: three_extractor(x[5]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["r_gaze_origin_in_user_coordinate_system_x", "r_gaze_origin_in_user_coordinate_system_y",
                 "r_gaze_origin_in_user_coordinate_system_z", ],
    )
    df_6 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[6]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["l_display_x", "l_display_y"], )
    df_7 = pd.DataFrame(
        ddf_eye_tracking.apply(lambda x: two_extractor(x[7]), meta=meta_type, axis=1).compute().transpose().tolist(),
        columns=["r_display_x", "r_display_y"], )
    df_8 = pd.DataFrame(ddf_eye_tracking[8].compute().transpose().tolist(), columns=["time"])
    df_9 = pd.DataFrame(ddf_eye_tracking[9].compute().transpose().tolist(), columns=["l_pupil_diameter"])
    df_10 = pd.DataFrame(ddf_eye_tracking[10].compute().transpose().tolist(), columns=["r_pupil_diameter"])

    # remove ddf_eye_tracking to save a bit of ram
    del ddf_eye_tracking

    # concat the dataframes to one eyetracking dataframe
    df_eye_tracking = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10], axis=1)

    print("(04/12) Normalize Eye Tracker Time", file=output, flush=True)
    # normalize the time to seconds
    t_0 = df_eye_tracking["time"][0]
    df_eye_tracking["time"] = (df_eye_tracking["time"].astype(float) - t_0) / 1000000.0

    # rescale the eeg data
    def rescale(eeg_data):
        if scaling_factor is None:
            return eeg_data
        # Scaling factor (to obtain values in [V], depends on device and settings etc.)
        return scaling_factor * eeg_data

    # Helper to read events from the info field directly; specific to some of our recordings
    def get_events_from_info(inst):
        eventsMNE = []
        eventsFromFIF = inst.info["events"]
        for i in range(0, len(eventsFromFIF)):
            if eventsFromFIF[i].get("list") is not None:
                content = eventsFromFIF[i].get("list")
                content_list = content.tolist()
                content_new = [content_list[2], content_list[1], content_list[0]]
                eventsMNE.append(content_new)
            elif eventsFromFIF[i].get("channels") is not None:
                raise
                # content = eventsFromFIF[i].get('channels')
            else:
                print("fiftools: Type of entry #" + str(i + 1) + "unkown.")
        eventsMNE = np.array(eventsMNE)
        return eventsMNE

    print("(05/12) Read EEG Data", file=output, flush=True)
    # read the eeg data and scale it
    raw = mne.io.read_raw_fif(fname=eeg_path, preload=True)

    print("(06/12) Preprocess EEG Data", file=output, flush=True)
    # Preprocessing: Scaling, Bandpass filter (0.5 to 80 Hz) and notch filter (power net frequency and harmonics)
    raw.apply_function(rescale, picks=["eeg"])
    if bandpass is not None:
        raw.filter(bandpass[0], bandpass[1])
    if notch is not None:
        raw.notch_filter([notch[0], notch[1]])

    print("(07/12) Construct Events from EEG Data", file=output, flush=True)
    # get the time of the events in seconds
    sampling_rate = raw.info["sfreq"]
    events = get_events_from_info(raw)
    event_ids = events[:, 2]
    indices_events = events[:, 0]
    t_events = event_ids / sampling_rate

    # save the event times in a dataframe for better handling
    columns = [
        "Snippet",
        "SnippetStart",
        "SnippetStop",
        "InputStart",
        "InputStop",
        "OutputStart",
        "OutputStop",
    ]
    df_time = pd.DataFrame([], columns=columns)
    for i in range(0, len(t_events)):
        if indices_events[i] > 100:
            continue
        df_time = df_time.append(pd.DataFrame(
            [[None, t_events[i + 1], t_events[i + 2], t_events[i + 2], t_events[i + 3], t_events[i + 3], None, ]],
            columns=columns, ))
    df_time = df_time.reset_index(drop=True)

    # extracts the file name from a path like "/test/path/file.txt" and returns "file"
    def to_file_name(path):
        file, _ext = os.path.splitext(path)
        return file.split("\\")[-1]

    # maps the answers from psychopy to better usable descriptors
    def map_to_answer(answer):
        if "Right" in answer:
            return "Right"
        if "Wrong1" in answer:
            return "Wrong1"
        if "Wrong2" in answer:
            return "Wrong2"
        if "None" in answer:
            return "Wrong3"
        if "Skipped" in answer:
            return "Skipped"

    print("(08/12) Read PsychoPy Data", file=output, flush=True)
    # read the data from the psychopy csv file
    df_psydata = pd.read_csv(psychopy_csv_path)

    print("(09/12) Transform PsychoPy Data", file=output, flush=True)
    # create a dataframe which holds the times and answers given for each snippet
    df_psydata = df_psydata[
        ["ImagePath", "Image.started", "Image.stopped", "InputPath", "image.started", "image.stopped",
         "ImagePathInputs", "image_1.started", "image_1.stopped", "ChoosenAnwer", "image_7.started", ]
    ]
    df_psydata = df_psydata[df_psydata["ImagePath"].notna()]
    df_psydata.insert(0, "Snippet", df_psydata["ImagePath"].apply(to_file_name))
    df_psydata["ChoosenAnwer"] = df_psydata["ChoosenAnwer"].apply(map_to_answer)
    df_psydata = df_psydata.reset_index(drop=True)
    df_psydata = df_psydata.rename(columns={"Image.started": "SnippetStart", "Image.stopped": "SnippetStop"})
    df_psydata = df_psydata.rename(columns={"image.started": "InputStart", "image.stopped": "InputStop"})
    df_psydata = df_psydata.rename(columns={"image_1.started": "OutputStart", "image_1.stopped": "OutputStop"})
    df_psydata = df_psydata.rename(columns={"image_7.started": "CrossStart"})
    df_psydata["SnippetStop"] = df_psydata["InputStart"]
    df_psydata["InputStop"] = df_psydata["OutputStart"]
    df_psydata["OutputStop"] = df_psydata["CrossStart"]
    df_psydata = df_psydata.drop(["ImagePath", "InputPath", "ImagePathInputs", "CrossStart"], axis=1)

    print("(10/12) Normalize PsychoPy Time", file=output, flush=True)
    # normalize the time of all the snippets
    start_time = df_psydata["SnippetStart"][0]
    df_psydata["SnippetStart"] = df_psydata["SnippetStart"] - start_time
    df_psydata["SnippetStop"] = df_psydata["SnippetStop"] - start_time
    df_psydata["InputStart"] = df_psydata["InputStart"] - start_time
    df_psydata["InputStop"] = df_psydata["InputStop"] - start_time
    df_psydata["OutputStart"] = df_psydata["OutputStart"] - start_time
    df_psydata["OutputStop"] = df_psydata["OutputStop"] - start_time

    print("(11/12) Read PsychoPy Log Data", file=output, flush=True)
    # read in the log file from psychopy
    df_psylog = pd.read_csv(psychopy_log_path, header=None, sep="\t")

    # five column names to the log file
    df_psylog.columns = ["time", "type", "message"]

    # normalize the time which of the psylog file
    df_psylog["time"] = df_psylog["time"] - start_time

    # set snippet name and the stop time of each snippet using deltas
    df_time["Snippet"] = df_psydata["Snippet"]
    df_time["OutputStop"] = df_time["OutputStart"] + df_psydata["OutputStop"] - df_psydata["OutputStart"]

    # store all the data in a dictionary for better handling. split everything up by snippet
    result = {}

    # just the template to know the layout of the dictionary
    template = {
        "Code": {"EyeTracking": None, "EEG": None, "Log": None, "Time": {"Start": None, "Stop": None, }, },
        "Input": {"EyeTracking": None, "EEG": None, "Log": None, "Time": {"Start": None, "Stop": None, }, },
        "Output": {"EyeTracking": None, "EEG": None, "Log": None, "Time": {"Start": None, "Stop": None, }, },
        "Behavioral": None,
    }

    print("(12/12) Transform All Data to Dictionary", file=output, flush=True)
    # iterate for every snippet to set the data
    for index, row in df_psydata.iterrows():
        current = template.copy()
        # add data for code
        current["Code"]["EyeTracking"] = df_eye_tracking[(df_eye_tracking["time"] >= df_time["SnippetStart"][index]) & (
                df_eye_tracking["time"] < df_time["SnippetStop"][index])]
        current["Code"]["EEG"] = raw.copy().crop(df_time["SnippetStart"][index], df_time["SnippetStop"][index])
        current["Code"]["Log"] = df_psylog[(df_psylog["time"] >= df_psydata["SnippetStart"][index]) & (
                df_psylog["time"] < df_psydata["SnippetStop"][index])]
        current["Code"]["Time"]["Start"] = df_psydata["SnippetStart"][index]
        current["Code"]["Time"]["Stop"] = df_psydata["SnippetStop"][index]

        # add data for input
        current["Input"]["EyeTracking"] = df_eye_tracking[(df_eye_tracking["time"] >= df_time["InputStart"][index]) & (
                df_eye_tracking["time"] < df_time["InputStop"][index])]
        current["Input"]["EEG"] = raw.copy().crop(df_time["InputStart"][index], df_time["InputStop"][index])
        current["Input"]["Log"] = df_psylog[(df_psylog["time"] >= df_psydata["InputStart"][index]) & (
                df_psylog["time"] < df_psydata["InputStop"][index])]
        current["Input"]["Time"]["Start"] = df_psydata["InputStart"][index]
        current["Input"]["Time"]["Stop"] = df_psydata["InputStop"][index]

        # add data for input
        current["Output"]["EyeTracking"] = df_eye_tracking[
            (df_eye_tracking["time"] >= df_time["OutputStart"][index]) & (
                    df_eye_tracking["time"] < df_time["OutputStop"][index])]
        current["Output"]["EEG"] = raw.copy().crop(df_time["OutputStart"][index], df_time["OutputStop"][index])
        current["Output"]["Log"] = df_psylog[(df_psylog["time"] >= df_psydata["OutputStart"][index]) & (
                df_psylog["time"] < df_psydata["OutputStop"][index])]
        current["Output"]["Time"]["Start"] = df_psydata["OutputStart"][index]
        current["Output"]["Time"]["Stop"] = df_psydata["OutputStop"][index]

        current["Behavioral"] = df_psydata.iloc[index].to_frame().transpose()
        result[row["Snippet"]] = current.copy()

    return result


def save(data_dictonary, participant_number, digits=2, logging=True):
    # setup paths for data saving
    general_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/"
    eye_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EyeTracker/"
    eeg_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EEG/"
    log_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/LOG/"
    behavioral_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/Behavioral/"
    meta_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/Meta/"

    # create folders if they dont exist
    Path(general_path).mkdir(parents=True, exist_ok=True)
    Path(eye_path).mkdir(parents=True, exist_ok=True)
    Path(eeg_path).mkdir(parents=True, exist_ok=True)
    Path(log_path).mkdir(parents=True, exist_ok=True)
    Path(behavioral_path).mkdir(parents=True, exist_ok=True)
    Path(meta_path).mkdir(parents=True, exist_ok=True)

    # set the stdout for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, 'w')

    # create new dictionary which will be used to save
    save = copy.deepcopy(data_dictonary)
    for entry in data_dictonary:
        # skip the meta entry
        if "_Meta" in entry:
            continue

        # save code
        print(f"Saving {entry} Files ...", end="", file=output, flush=True)
        data_dictonary[entry]["Code"]["EyeTracking"].to_excel(eye_path + "Code_" + entry + ".xlsx", index=False)
        save[entry]["Code"]["EyeTracking"] = eye_path + "Code_" + entry + ".xlsx"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Code"]["EEG"].save(eeg_path + "Code_" + entry + "_raw.fif", overwrite=True)
        save[entry]["Code"]["EEG"] = eeg_path + "Code_" + entry + "_raw.fif"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Code"]["Log"].to_excel(log_path + "Code_" + entry + ".xlsx", index=False)
        save[entry]["Code"]["Log"] = log_path + "Code_" + entry + ".xlsx"

        # save input
        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Input"]["EyeTracking"].to_excel(eye_path + "Input_" + entry + ".xlsx", index=False)
        save[entry]["Input"]["EyeTracking"] = eye_path + "Input_" + entry + ".xlsx"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Input"]["EEG"].save(eeg_path + "Input_" + entry + "_raw.fif", overwrite=True)
        save[entry]["Input"]["EEG"] = eeg_path + "Input_" + entry + "_raw.fif"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Input"]["Log"].to_excel(log_path + "Input_" + entry + ".xlsx", index=False)
        save[entry]["Input"]["Log"] = log_path + "Input_" + entry + ".xlsx"

        # save output
        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Output"]["EyeTracking"].to_excel(eye_path + "Output_" + entry + ".xlsx", index=False)
        save[entry]["Output"]["EyeTracking"] = eye_path + "Output_" + entry + ".xlsx"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Output"]["EEG"].save(eeg_path + "Output_" + entry + "_raw.fif", overwrite=True)
        save[entry]["Output"]["EEG"] = eeg_path + "Output_" + entry + "_raw.fif"

        print(".", end="", file=output, flush=True)
        data_dictonary[entry]["Output"]["Log"].to_excel(log_path + "Output_" + entry + ".xlsx", index=False)
        save[entry]["Output"]["Log"] = log_path + "Output_" + entry + ".xlsx"

        # save behavioral
        print(".", file=output, flush=True)
        data_dictonary[entry]["Behavioral"].to_excel(behavioral_path + entry + ".xlsx", index=False)
        save[entry]["Behavioral"] = behavioral_path + entry + ".xlsx"

    # save file
    with open(general_path + "DataBase.json", "w") as fp:
        json.dump(save, fp, indent=4, sort_keys=True)


def load_all(participant_number, digits=2, logging=True):
    # setup paths for data saving
    json_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/" + "DataBase.json"
    eye_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EyeTracker/"
    eeg_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EEG/"
    log_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/LOG/"
    behavioral_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/Behavioral/"
    meta_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/Meta/"

    result = {}
    with open(json_path) as json_file:
        result = json.load(json_file)

    # set the stdout for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, 'w')

    # read all the data
    for entry in result:
        if "_Meta" in entry:
            continue

        # load code
        print(f"Loading {entry} Files ...", end="", file=output, flush=True)
        result[entry]["Code"]["EyeTracking"] = pd.read_excel(eye_path + "Code_" + entry + ".xlsx")

        print(".", end="", file=output, flush=True)
        result[entry]["Code"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Code_" + entry + "_raw.fif")

        print(".", end="", file=output, flush=True)
        result[entry]["Code"]["Log"] = pd.read_excel(log_path + "Code_" + entry + ".xlsx")

        # load input
        print(".", end="", file=output, flush=True)
        result[entry]["Input"]["EyeTracking"] = pd.read_excel(eye_path + "Input_" + entry + ".xlsx")

        print(".", end="", file=output, flush=True)
        result[entry]["Input"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Input_" + entry + "_raw.fif")

        print(".", end="", file=output, flush=True)
        result[entry]["Input"]["Log"] = pd.read_excel(log_path + "Input_" + entry + ".xlsx")

        # load output
        print(".", end="", file=output, flush=True)
        result[entry]["Output"]["EyeTracking"] = pd.read_excel(eye_path + "Output_" + entry + ".xlsx")

        print(".", end="", file=output, flush=True)
        result[entry]["Output"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Output_" + entry + "_raw.fif")

        print(".", end="", file=output, flush=True)
        result[entry]["Output"]["Log"] = pd.read_excel(log_path + "Output_" + entry + ".xlsx")

        # load behavioral
        print(".", file=output, flush=True)
        result[entry]["Behavioral"] = pd.read_excel(behavioral_path + entry + ".xlsx")

    return result


def load_queried(participant_number, digits=2, logging=True, snippets=None, query_eeg=False, query_eye_tracking=False,
                 query_log=False, query_behavioral=False, query_code=False, query_input=False,
                 query_output=False):
    # setup paths for data saving
    if snippets is None:
        snippets = []
    json_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/" + "DataBase.json"
    eye_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EyeTracker/"
    eeg_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/EEG/"
    log_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/LOG/"
    behavioral_path = f"./filteredData/Participant{str(participant_number).zfill(digits)}/Behavioral/"

    result = {}
    with open(json_path) as json_file:
        result = json.load(json_file)

    # set the stdout for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, 'w')

    # read all the data
    save = copy.deepcopy(result)
    for entry in save:
        if entry not in snippets:
            del result[entry]
            continue

        # load code
        print(f"Loading {entry} Files ...", end="", file=output, flush=True)
        if query_code:
            if query_eye_tracking:
                result[entry]["Code"]["EyeTracking"] = pd.read_excel(eye_path + "Code_" + entry + ".xlsx")
            else:
                del result[entry]["Code"]["EyeTracking"]

            print(".", end="", file=output, flush=True)
            if query_eeg:
                result[entry]["Code"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Code_" + entry + "_raw.fif")
            else:
                del result[entry]["Code"]["EEG"]

            print(".", end="", file=output, flush=True)
            if query_log:
                result[entry]["Code"]["Log"] = pd.read_excel(log_path + "Code_" + entry + ".xlsx")
            else:
                del result[entry]["Code"]["Log"]
        else:
            del result[entry]["Code"]

        # load input
        if query_input:
            print(".", end="", file=output, flush=True)
            if query_eye_tracking:
                result[entry]["Input"]["EyeTracking"] = pd.read_excel(eye_path + "Input_" + entry + ".xlsx")
            else:
                del result[entry]["Input"]["EyeTracking"]

            print(".", end="", file=output, flush=True)
            if query_eeg:
                result[entry]["Input"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Input_" + entry + "_raw.fif")
            else:
                del result[entry]["Input"]["EEG"]

            print(".", end="", file=output, flush=True)
            if query_log:
                result[entry]["Input"]["Log"] = pd.read_excel(log_path + "Input_" + entry + ".xlsx")
            else:
                del result[entry]["Input"]["Log"]
        else:
            del result[entry]["Input"]

        # load output
        if query_output:
            print(".", end="", file=output, flush=True)
            if query_eye_tracking:
                result[entry]["Output"]["EyeTracking"] = pd.read_excel(eye_path + "Output_" + entry + ".xlsx")
            else:
                del result[entry]["Output"]["EyeTracking"]

            print(".", end="", file=output, flush=True)
            if query_eeg:
                result[entry]["Output"]["EEG"] = mne.io.read_raw_fif(eeg_path + "Output_" + entry + "_raw.fif")
            else:
                del result[entry]["Output"]["EEG"]

            print(".", end="", file=output, flush=True)
            if query_log:
                result[entry]["Output"]["Log"] = pd.read_excel(log_path + "Output_" + entry + ".xlsx")
            else:
                del result[entry]["Output"]["Log"]
        else:
            del result[entry]["Output"]

        # load behavioral
        if query_behavioral:
            print(".", file=output, flush=True)
            result[entry]["Behavioral"] = pd.read_excel(behavioral_path + entry + ".xlsx")
        else:
            del result[entry]["Behavioral"]

    return result
