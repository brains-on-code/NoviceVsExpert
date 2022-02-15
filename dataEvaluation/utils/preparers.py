import os
import mne
import re
import dask.dataframe as dd
import numpy as np
import pandas as pd
import sys

mne.set_log_level("WARNING")


def load_raw(participant_number, cores=12, digits=2, logging=True,
             raw_path="./data/rawData/"):
    # setup output for logging
    output = sys.stdout
    if not logging:
        output = open(os.devnull, 'w')

    print("(01/10) Construct Paths", file=output, flush=True)
    # setup paths for loading
    participant_folder = raw_path + "Participant" + str(participant_number).zfill(digits) + "/"
    eye_tracking_path = participant_folder + "eyetracking_raw.csv"
    eeg_path = participant_folder + "eeg_raw.fif"
    eeg_set_path = participant_folder + "eeg_raw_" + str(participant_number).zfill(digits) + ".set"
    psychopy_csv_path = participant_folder + "experiment.csv"

    print("(02/10) Read Eye Tracker Data", file=output, flush=True)
    # read tracker data
    df_eye_tracking = pd.read_csv(eye_tracking_path, header=None, sep=";")

    # setup regex for number extraction
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

    print("(03/10) Transform Eye Tracker Data", file=output, flush=True)
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

    print("(04/10) Normalize Eye Tracker Time", file=output, flush=True)
    # normalize the time to seconds
    t_0 = df_eye_tracking["time"][0]
    df_eye_tracking["time"] = (df_eye_tracking["time"].astype(float) - t_0) / 1000000.0

    # Helper to read events from the info field directly; specific to some of our recordings
    def get_events_from_info(inst):
        eventsMNE = []
        eventsFromFIF = inst.info["events"]
        for event_idx in range(0, len(eventsFromFIF)):
            if eventsFromFIF[event_idx].get("list") is not None:
                content = eventsFromFIF[event_idx].get("list")
                content_list = content.tolist()
                content_new = [content_list[2], content_list[1], content_list[0]]
                eventsMNE.append(content_new)
            elif eventsFromFIF[event_idx].get("channels") is not None:
                raise
                # content = eventsFromFIF[i].get('channels')
            else:
                print("fiftools: Type of entry #" + str(event_idx + 1) + "unknown.")
        eventsMNE = np.array(eventsMNE)
        return eventsMNE

    print("(05/10) Read EEG Data", file=output, flush=True)
    # read the eeg data and scale it
    raw = mne.io.read_raw_fif(fname=eeg_path, preload=True)
    raw_set = mne.io.read_raw_eeglab(eeg_set_path, preload=True)

    print("(06/10) Construct Events from EEG Data", file=output, flush=True)
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

    print("(07/10) Read PsychoPy Data", file=output, flush=True)
    # read the data from the psychopy csv file
    df_psydata = pd.read_csv(psychopy_csv_path)

    print("(08/10) Transform PsychoPy Data", file=output, flush=True)
    # create a dataframe which holds the times and answers given for each snippet
    df_psydata = df_psydata[
        ["ImagePath", "Image.started", "Image.stopped", "InputPath", "image.started", "image.stopped",
         "ImagePathInputs", "image_1.started", "image_1.stopped", "ChoosenAnwer", "image_7.started", ]
    ]
    df_psydata = df_psydata[df_psydata["ImagePath"].notna()]
    df_psydata.insert(0, "Snippet", df_psydata["ImagePath"].apply(to_file_name))
    df_psydata["ChoosenAnwer"] = df_psydata["ChoosenAnwer"].apply(map_to_answer)
    df_psydata = df_psydata.rename(columns={"ChoosenAnwer": "ChosenAnswer"})
    df_psydata = df_psydata.reset_index(drop=True)
    df_psydata = df_psydata.rename(columns={"Image.started": "SnippetStart", "Image.stopped": "SnippetStop"})
    df_psydata = df_psydata.rename(columns={"image.started": "InputStart", "image.stopped": "InputStop"})
    df_psydata = df_psydata.rename(columns={"image_1.started": "OutputStart", "image_1.stopped": "OutputStop"})
    df_psydata = df_psydata.rename(columns={"image_7.started": "CrossStart"})
    df_psydata["SnippetStop"] = df_psydata["InputStart"]
    df_psydata["InputStop"] = df_psydata["OutputStart"]
    df_psydata["OutputStop"] = df_psydata["CrossStart"]
    df_psydata = df_psydata.drop(["ImagePath", "InputPath", "ImagePathInputs", "CrossStart"], axis=1)

    print("(9/10) Normalize PsychoPy Time", file=output, flush=True)
    # normalize the time of all the snippets
    start_time = df_psydata["SnippetStart"][0]
    df_psydata["SnippetStart"] = df_psydata["SnippetStart"] - start_time
    df_psydata["SnippetStop"] = df_psydata["SnippetStop"] - start_time
    df_psydata["InputStart"] = df_psydata["InputStart"] - start_time
    df_psydata["InputStop"] = df_psydata["InputStop"] - start_time
    df_psydata["OutputStart"] = df_psydata["OutputStart"] - start_time
    df_psydata["OutputStop"] = df_psydata["OutputStop"] - start_time

    # set snippet name and the stop time of each snippet using deltas
    df_time["Snippet"] = df_psydata["Snippet"]
    df_time["OutputStop"] = df_time["OutputStart"] + df_psydata["OutputStop"] - df_psydata["OutputStart"]

    # store all the data in a dictionary for better handling. split everything up by snippet
    result = {}

    # just the template to know the layout of the dictionary

    print("(10/10) Transform All Data to Dictionary", file=output, flush=True)
    # iterate for every snippet to set the data
    for index, row in df_psydata.iterrows():
        current = {"Code": {"EyeTracking": None, "EEG": None, "Time": {"Start": None, "Stop": None, }, },
                   "Input": {"EyeTracking": None, "EEG": None, "Time": {"Start": None, "Stop": None, }, },
                   "Output": {"EyeTracking": None, "EEG": None, "Time": {"Start": None, "Stop": None, }, },
                   "Behavioral": None}

        # add data for code
        current["Code"]["EyeTracking"] = df_eye_tracking[(df_eye_tracking["time"] >= df_time["SnippetStart"][index]) & (
                df_eye_tracking["time"] < df_time["SnippetStop"][index])]
        current["Code"]["EEG"] = raw_set.copy().crop(df_time["SnippetStart"][index], df_time["SnippetStop"][index])
        current["Code"]["Time"]["Start"] = df_psydata["SnippetStart"][index]
        current["Code"]["Time"]["Stop"] = df_psydata["SnippetStop"][index]

        # add data for input
        current["Input"]["EyeTracking"] = df_eye_tracking[(df_eye_tracking["time"] >= df_time["InputStart"][index]) & (
                df_eye_tracking["time"] < df_time["InputStop"][index])]
        current["Input"]["EEG"] = raw_set.copy().crop(df_time["InputStart"][index], df_time["InputStop"][index])
        current["Input"]["Time"]["Start"] = df_psydata["InputStart"][index]
        current["Input"]["Time"]["Stop"] = df_psydata["InputStop"][index]

        # add data for input
        current["Output"]["EyeTracking"] = df_eye_tracking[
            (df_eye_tracking["time"] >= df_time["OutputStart"][index]) & (
                    df_eye_tracking["time"] < df_time["OutputStop"][index])]
        current["Output"]["EEG"] = raw_set.copy().crop(df_time["OutputStart"][index], df_time["OutputStop"][index])
        current["Output"]["Time"]["Start"] = df_psydata["OutputStart"][index]
        current["Output"]["Time"]["Stop"] = df_psydata["OutputStop"][index]

        current["Behavioral"] = df_psydata.iloc[index].to_frame().transpose()
        result[row["Snippet"]] = current

    return result
