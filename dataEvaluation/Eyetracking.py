import warnings
import matplotlib
import pandas as pd

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import preparers
import os
import regex as re
import sonaion_analysis as son
from pandas.core.common import SettingWithCopyWarning
import GenSnippetsLib as snippet

warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

# prepare global variables for settings
denoise_degree = 10
display_width = 1920
display_height = 1080
d_time = 0.004
treshhold_for_fixation = 2400.0

left_color = (1.0, 0.0, 0.0)
left_saccades_color = (0.0, 1.0, 1.0)
left_fixxation_color = (1.0, 0.0, 0.0)

right_color = (0.0, 1.0, 0.0)
right_saccades_color = (1.0, 0.0, 1.0)
right_fixxation_color = (0.0, 1.0, 0.0)

generator_path = "../CodeSnippets/Generators/"
img_dict = {}
img_quantify_dict = {}

# get all first level folders from the data folder
folders = os.listdir("./filteredData")

# compile a regex to find all numbers in folder names
regex = re.compile(r'\d+')

# create a list of all the numbers in the folder names
numbers = [int(regex.findall(folder)[0]) for folder in folders if "." not in folder]


def mask_function():
    return lambda height, width, coordinate: son.utils.masks.create_circular_mask(height, width, coordinate, 30)


def interpolate(start_color, end_color, current, max_value):
    t = current / float(max_value)
    r = (1.0 - t) * start_color[0] + t * end_color[0]
    g = (1.0 - t) * start_color[1] + t * end_color[1]
    b = (1.0 - t) * start_color[2] + t * end_color[2]
    return (r, g, b)

print()
# iterate over all the numbers and perform the eyetracking analysis
for number in numbers:
    print("Analyzing data from participant " + str(number))

    # load the data
    print("\tLoading data...")
    data = preparers.load_queried(
        participant_number=number,
        snippets=["Ackerman"],
        query_code=True,
        query_eye_tracking=True,
        query_behavioral=True,
        logging=False
    )

    # iterate over every snippet from the eyetracking data and perform the analysis
    for key in data.keys():
        print("\t\tWorking with data ", key, "...")
        #create a folder for the current snippet
        snippet_folder = r"./result/{}/Participant_{}".format(key, number)

        # create folder if it does not exist
        if not os.path.exists(snippet_folder):
            os.makedirs(snippet_folder)


        # check if key in img_dict, otherwise generate image
        if key not in img_dict:
            img, result = snippet.create_image(generator_path + key + ".json", font_path="/../CodeSnippets/fonts/ttf/")
            bg = snippet.create_background(display_width, display_height, (180, 180, 180, 255))
            img = snippet.place_image_on(bg, np.array(img), 0.5, 0.5)
            img_dict[key] = img
            img_quantify_dict[key] = pd.DataFrame([], columns=[
                "Left Saccades Count",
                "Left Time to First Saccade",
                "Left Average Saccade Time",
                "Left Fixation Count",
                "Left Time to First Fixation",
                "Left Average Fixation Time",
                "Right Saccades Count",
                "Right Time to First Saccade",
                "Right Average Saccade Time",
                "Right Fixation Count",
                "Right Time to First Fixation",
                "Right Average Fixation Time",
            ])

        # get the current image
        img = img_dict[key]

        # prepare queried data
        df_eyetracking = data[key]["Code"]["EyeTracking"][
            [
                "l_valid",
                "r_valid",
                "l_display_x",
                "l_display_y",
                "r_display_x",
                "r_display_y",
                "time",
                "l_pupil_diameter",
                "r_pupil_diameter",
            ]
        ]

        # transform the eye data to the display coordinates
        df_eyetracking["l_display_x"] = df_eyetracking["l_display_x"].apply(lambda x: x * display_width)
        df_eyetracking["l_display_x"] = df_eyetracking["l_display_x"].astype(float).fillna(0).astype(int)

        df_eyetracking["r_display_x"] = df_eyetracking["r_display_x"].apply(lambda x: x * display_width)
        df_eyetracking["r_display_x"] = df_eyetracking["r_display_x"].astype(float).fillna(0).astype(int)

        df_eyetracking["l_display_y"] = df_eyetracking["l_display_y"].apply(lambda x: x * display_height)
        df_eyetracking["l_display_y"] = df_eyetracking["l_display_y"].astype(float).fillna(0).astype(int)

        df_eyetracking["r_display_y"] = df_eyetracking["r_display_y"].apply(lambda x: x * display_height)
        df_eyetracking["r_display_y"] = df_eyetracking["r_display_y"].astype(float).fillna(0).astype(int)

        # normalize the time
        df_eyetracking["time"] = df_eyetracking["time"] - df_eyetracking["time"][0]

        # replace invalid data with previous valid data for the right eye
        (replaced_r_x, replaced_r_y, replaced_r_diameter,
         replaced_r_valid) = son.eyetracking.preprocessing_invalid.replace_with_prev_invalid(
            df_eyetracking["r_display_x"],
            df_eyetracking["r_display_y"],
            df_eyetracking["r_pupil_diameter"],
            df_eyetracking["r_valid"],
        )

        # update the dataframe with the replaced values
        df_eyetracking["r_display_x"] = replaced_r_x
        df_eyetracking["r_display_y"] = replaced_r_y
        df_eyetracking["r_pupil_diameter"] = replaced_r_diameter
        df_eyetracking["r_valid"] = replaced_r_valid

        # replace invalid data with previous valid data for the left eye
        (replaced_l_x, replaced_l_y, replaced_l_diameter,
         replaced_l_valid) = son.eyetracking.preprocessing_invalid.replace_with_prev_invalid(
            df_eyetracking["l_display_x"],
            df_eyetracking["l_display_y"],
            df_eyetracking["l_pupil_diameter"],
            df_eyetracking["l_valid"],
        )

        # update the dataframe with the replaced values
        df_eyetracking["l_display_x"] = replaced_l_x
        df_eyetracking["l_display_y"] = replaced_l_y
        df_eyetracking["l_pupil_diameter"] = replaced_l_diameter
        df_eyetracking["l_valid"] = replaced_l_valid

        # denoise the eyetracking data
        for _i in range(denoise_degree):
            # denoise the right eye
            denoised_r_x, denoised_r_y = son.eyetracking.preprocessing_denoise.denoise(
                df_eyetracking["r_display_x"],
                df_eyetracking["r_display_y"],
                son.eyetracking.preprocessing_denoise.parabola_5_kernel
            )

            # update the dataframe with the denoised values
            df_eyetracking["r_display_x"] = denoised_r_x
            df_eyetracking["r_display_y"] = denoised_r_y

            # denoise the left eye
            denoised_l_x, denoised_l_y = son.eyetracking.preprocessing_denoise.denoise(
                df_eyetracking["l_display_x"],
                df_eyetracking["l_display_y"],
                son.eyetracking.preprocessing_denoise.parabola_5_kernel
            )

            # update the dataframe with the denoised values
            df_eyetracking["l_display_x"] = denoised_l_x
            df_eyetracking["l_display_y"] = denoised_l_y

        # create heatmaps
        data_left = son.eyetracking.heatmap.create_heatmap(
            df_eyetracking["l_display_x"],
            df_eyetracking["l_display_y"],
            df_eyetracking["l_valid"],
            0.004,
            display_width,
            display_height,
            mask_function(),
        )

        data_right = son.eyetracking.heatmap.create_heatmap(
            df_eyetracking["r_display_x"],
            df_eyetracking["r_display_y"],
            df_eyetracking["r_valid"],
            0.004,
            display_width,
            display_height,
            mask_function(),
        )

        data_left = data_left / data_left.max()
        data_right = data_right / data_right.max()

        data_right = np.array(
            [data_right * right_color[0], data_right * right_color[1], data_right * right_color[2], data_right])
        data_right = np.moveaxis(data_right, 0, 2)

        data_left = np.array(
            [data_left * left_color[0], data_left * left_color[1], data_left * left_color[2], data_left])
        data_left = np.moveaxis(data_left, 0, 2)

        # save heatmaps
        # left eye
        fig, ax = plt.subplots()
        ax.imshow(data_left, zorder=2, alpha=0.5)
        ax.imshow(img, zorder=1)
        plt.title("Left eye Heatmap")
        plt.savefig(snippet_folder + "/" + "LeftEyeHeatmap.pdf", dpi=300)

        # right eye
        fig, ax = plt.subplots()
        ax.imshow(data_right, zorder=2, alpha=0.5)
        ax.imshow(img, zorder=1)
        plt.title("Right eye Heatmap")
        plt.savefig(snippet_folder + "/" + "RightEyeHeatmap.pdf", dpi=300)

        # create sequence diagrams

        data_right = son.eyetracking.sequence.create_sequence_diagram_y(
            df_eyetracking["r_display_y"],
            df_eyetracking["r_valid"],
            display_height,
            display_width,
            offset=10,
            step=0.1,
            should_skip=True,
        )
        data_right = np.array(
            [data_right * right_color[0], data_right * right_color[1], data_right * right_color[2], data_right])
        data_right = np.moveaxis(data_right, 0, 2)

        data_left = son.eyetracking.sequence.create_sequence_diagram_y(
            df_eyetracking["l_display_y"],
            df_eyetracking["l_valid"],
            display_height,
            display_width,
            offset=10,
            step=0.1,
            should_skip=False,
        )
        data_left = np.array(
            [data_left * left_color[0], data_left * left_color[1], data_left * left_color[2], data_left])
        data_left = np.moveaxis(data_left, 0, 2)

        # save sequence diagrams
        # left eye
        fig, ax = plt.subplots()
        ax.imshow(data_left, zorder=2, alpha=0.5)
        plt.title("Left eye Sequence Diagram")
        ax.imshow(img, zorder=1)
        plt.savefig(snippet_folder + "/" + "LeftEyeSequenceDiagram.pdf", dpi=300)

        # right eye
        fig, ax = plt.subplots()
        ax.imshow(data_right, zorder=3, alpha=0.5)
        ax.imshow(img, zorder=1)
        plt.title("Right eye Sequence Diagram")
        plt.savefig(snippet_folder + "/" + "RightEyeSequenceDiagram.pdf", dpi=300)

        # classify saccades and fixations
        # right eye
        right_saccades_color = (1.0, 0.0, 1.0)
        right_fixxation_color = (0.0, 1.0, 0.0)
        saccades_r = son.eyetracking.metrics.classify_saccades(
            df_eyetracking["r_display_x"], df_eyetracking["r_display_y"], d_time, treshhold_for_fixation
        )
        saccades_r[0] = saccades_r[1]
        fixxation_r = son.eyetracking.metrics.classify_fixxation(
            df_eyetracking["r_display_x"], df_eyetracking["r_display_y"], d_time, treshhold_for_fixation
        )
        fixxation_r[0] = fixxation_r[1]

        saccades_r = np.array(saccades_r)
        fixxation_r = np.array(fixxation_r)
        classificator_right = np.add(saccades_r, np.multiply(fixxation_r, 2))

        # left eye
        saccades_l = son.eyetracking.metrics.classify_saccades(
            df_eyetracking["l_display_x"], df_eyetracking["l_display_y"], d_time, treshhold_for_fixation
        )
        saccades_l[0] = saccades_l[1]
        fixxation_l = son.eyetracking.metrics.classify_fixxation(
            df_eyetracking["l_display_x"], df_eyetracking["l_display_y"], d_time, treshhold_for_fixation
        )
        fixxation_l[0] = fixxation_l[1]

        saccades_l = np.array(saccades_l)
        fixxation_l = np.array(fixxation_l)
        classificator_left = np.add(saccades_l, np.multiply(fixxation_l, 2))

        # create fixxation sequence diagrams
        data_right = son.eyetracking.sequence.create_classified_sequence_diagram_y(
            df_eyetracking["r_display_y"], classificator_right, display_height, display_width, offset=10, step=0.1
        )

        data_right_saccades = np.array(data_right).astype(int)
        data_right_saccades[np.where(data_right_saccades == 2)] = 0
        data_right_saccades = np.array(
            [
                data_right_saccades * right_saccades_color[0],
                data_right_saccades * right_saccades_color[1],
                data_right_saccades * right_saccades_color[2],
                data_right_saccades,
            ]
        )
        data_right_saccades = np.moveaxis(data_right_saccades, 0, 2)

        data_right_fixxations = np.array(data_right).astype(int)
        data_right_fixxations[np.where(data_right_fixxations == 1)] = 0
        data_right_fixxations = data_right_fixxations / 2
        data_right_fixxations = np.array(
            [
                data_right_fixxations * right_fixxation_color[0],
                data_right_fixxations * right_fixxation_color[1],
                data_right_fixxations * right_fixxation_color[2],
                data_right_fixxations,
            ]
        )
        data_right_fixxations = np.moveaxis(data_right_fixxations, 0, 2)

        data_left = son.eyetracking.sequence.create_classified_sequence_diagram_y(
            df_eyetracking["l_display_y"], classificator_left, display_height, display_width, offset=10, step=0.1
        )

        data_left_saccades = np.array(data_left).astype(int)
        data_left_saccades[np.where(data_left_saccades == 2)] = 0
        data_left_saccades = np.array(
            [
                data_left_saccades * left_saccades_color[0],
                data_left_saccades * left_saccades_color[1],
                data_left_saccades * left_saccades_color[2],
                data_left_saccades,
            ]
        )
        data_left_saccades = np.moveaxis(data_left_saccades, 0, 2)

        data_left_fixxations = np.array(data_left).astype(int)
        data_left_fixxations[np.where(data_left_fixxations == 1)] = 0
        data_left_fixxations = data_left_fixxations / 2
        data_left_fixxations = np.array(
            [
                data_left_fixxations * left_fixxation_color[0],
                data_left_fixxations * left_fixxation_color[1],
                data_left_fixxations * left_fixxation_color[2],
                data_left_fixxations,
            ]
        )
        data_left_fixxations = np.moveaxis(data_left_fixxations, 0, 2)

        # save sequence diagrams
        # left eye
        fig, ax = plt.subplots()
        ax.imshow(data_left_fixxations, zorder=2, alpha=0.8)
        ax.imshow(data_left_saccades, zorder=2, alpha=0.8)
        ax.imshow(img, zorder=1)
        plt.title("Left eye Fixation/Saccades Sequence Diagram")
        plt.savefig(snippet_folder + "/" + "LeftEyeFixationSaccadesSequenceDiagram.pdf", dpi=300)

        # right eye
        fig, ax = plt.subplots()
        ax.imshow(data_right_fixxations, zorder=2, alpha=0.8)
        ax.imshow(data_right_saccades, zorder=2, alpha=0.8)
        ax.imshow(img, zorder=1)
        plt.title("Right eye Fixation/Saccades Sequence Diagram")
        plt.savefig(snippet_folder + "/" + "RightEyeFixationSaccadesSequenceDiagram.pdf", dpi=300)

        # save quantified values diagrams
        img_quantify_dict[key] = img_quantify_dict[key].append(pd.DataFrame([[
            son.eyetracking.metrics.count_saccades(saccades_l),
            son.eyetracking.metrics.time_of_saccades(saccades_l, d_time)[0][0],
            son.eyetracking.metrics.average_saccades_time(son.eyetracking.metrics.time_of_saccades(saccades_l, d_time)),
            son.eyetracking.metrics.count_saccades(fixxation_l),
            son.eyetracking.metrics.time_of_saccades(fixxation_l, d_time)[0][0],
            son.eyetracking.metrics.average_saccades_time(son.eyetracking.metrics.time_of_saccades(fixxation_l, d_time)),

            son.eyetracking.metrics.count_saccades(saccades_r),
            son.eyetracking.metrics.time_of_saccades(saccades_r, d_time)[0][0],
            son.eyetracking.metrics.average_saccades_time(son.eyetracking.metrics.time_of_saccades(saccades_r, d_time)),
            son.eyetracking.metrics.count_saccades(fixxation_r),
            son.eyetracking.metrics.time_of_saccades(fixxation_r, d_time)[0][0],
            son.eyetracking.metrics.average_saccades_time(son.eyetracking.metrics.time_of_saccades(fixxation_r, d_time)),
        ]], columns=img_quantify_dict[key].columns))


        # create fixation map
        fixxation_map_l = son.eyetracking.fixxationmap.create_fixxation_map(df_eyetracking["l_display_x"],
                                                                            df_eyetracking["l_display_y"], fixxation_l)
        fixxation_map_r = son.eyetracking.fixxationmap.create_fixxation_map(df_eyetracking["r_display_x"],
                                                                            df_eyetracking["r_display_y"], fixxation_r)

        # plot fixxation map
        # left eye
        fig, ax = plt.subplots()
        x_val = [float(int(x)) for ((x, _), _, _) in fixxation_map_l]
        y_val = [float(int(y)) for ((_, y), _, _) in fixxation_map_l]

        for i in range(len(x_val) - 2):
            ax.plot(
                x_val[i: i + 2],
                y_val[i: i + 2],
                "-",
                color=interpolate(left_color, (0.0, 0.0, 0.0), i, len(x_val)),
                zorder=2,
                alpha=0.6,
            )

        filtered_x_val = [float(int(x)) for ((x, _), _, flag) in fixxation_map_l if flag]
        filtered_y_val = [float(int(y)) for ((_, y), _, flag) in fixxation_map_l if flag]
        ax.scatter(
            filtered_x_val,
            filtered_y_val,
            4,
            c=[
                interpolate(left_color, (0.0, 0.0, 0.0), idx, len(x_val))
                for idx, (_, _, flag) in enumerate(fixxation_map_l)
                if flag
            ],
            zorder=3,
            alpha=0.6,
        )
        ax.imshow(img, zorder=1)
        plt.title("Left eye Fixation Map")
        plt.savefig(snippet_folder + "/" + "LeftEyeFixationMap.pdf", dpi=300)

        # right eye
        fig, ax = plt.subplots()
        x_val = [float(int(x)) for ((x, _), _, _) in fixxation_map_r]
        y_val = [float(int(y)) for ((_, y), _, _) in fixxation_map_r]

        for i in range(len(x_val) - 2):
            ax.plot(
                x_val[i: i + 2],
                y_val[i: i + 2],
                "-",
                color=interpolate(right_color, (0.0, 0.0, 0.0), i, len(x_val)),
                zorder=2,
                alpha=0.6,
            )

        filtered_x_val = [float(int(x)) for ((x, _), _, flag) in fixxation_map_r if flag]
        filtered_y_val = [float(int(y)) for ((_, y), _, flag) in fixxation_map_r if flag]
        ax.scatter(
            filtered_x_val,
            filtered_y_val,
            4,
            c=[
                interpolate(right_color, (0.0, 0.0, 0.0), idx, len(x_val))
                for idx, (_, _, flag) in enumerate(fixxation_map_r)
                if flag
            ],
            zorder=3,
            alpha=0.6,
        )
        ax.imshow(img, zorder=1)
        plt.title("Right eye Fixation Map")
        plt.savefig(snippet_folder + "/" + "RightEyeFixationMap.pdf", dpi=300)

for key in img_quantify_dict.keys():
    snippet_folder = r"./result/{}/".format(key)
    img_quantify_dict[key].to_excel(snippet_folder + "Metrics.xlsx")

print("Done!")
