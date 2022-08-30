# Data Evaluation

Pipeline Describes

---

## [Preprocessing 01](Preprocessing01_fif_to_set.ipynb)

Converts all the **.fif** files to **.set** files. This is done to do an automated ICA and filtering via Matlab/EEGlab 

## [Preprocessing 02](Preprocessing02_ICA.ipynb)

Apply Notch 2,200 Hz filter and perform an ICA on the eeg data.

## [Preprocessing 03](Preprocessing03_data_format.ipynb)

Split the Data into a workable format for the rest of the pipeline.
Therefore Data is splitted for each task into 
{Eyetracking, EEG, Behavioral}x{Code, Input, Output}x{CrossFixationBaseline}x{Answer}

## [Preprocessing 04](Preprocessing04_skill_score.ipynb)

Calculate the skill score for each Participant. Using correct answers per minute.

## [Preprocessing 05](Preprocessing05_fixxation_detection.ipynb)

Calculate the fixation for each Participant using I2MC algorithm.

## [RQ1](RQ1_PAPER_Eyetracking.ipynb)

Calculate the Metrics needed for RQ1.

## [RQ2](RQ2_PAPER_EEG.ipynb)

Calculate the Metrics needed for RQ2.




