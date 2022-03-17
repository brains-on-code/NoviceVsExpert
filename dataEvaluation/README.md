# Data Evaluation

---

## [Preprocessing 01](Preprocessing01_fif_to_set.ipynb)

Converts all the EEG **.fif** files to **.set** files. This is necessary to conduct an automated ICA and filtering via Matlab/EEGlab.

## [Preprocessing 02](Preprocessing02_ICA.ipynb)

Applies a notch 2-200 Hz filter and perform an ICA on the EEG data.

## [Preprocessing 03](Preprocessing03_data_format.ipynb)

Splits the data into a workable format for the rest of the pipeline. To this end, the data are splitted for each task into:
{Eyetracking, EEG, Behavioral}x{Code, Input, Output}x{CrossFixationBaseline}x{Answer}

## [Preprocessing 04](Preprocessing04_skill_score.ipynb)

Calculates the efficacy (here: skill score) for each participant.

## [Preprocessing 05](Preprocessing05_fixxation_detection.ipynb)

Calculates the fixations and saccedes for each participant using I2MC algorithm.

## [RQ1](RQ1_Eyetracking.ipynb)

Calculates the measures needed for RQ1.

## [RQ2](RQ2_EEG.ipynb)

Calculates the measures needed for RQ2.

## [RQ3](RQ3_ExperienceMeasures.ipynb)

Calculates the correlations needed for RQ3.


