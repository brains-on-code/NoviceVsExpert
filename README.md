# Correlates of Programmer Efficacy and Their Link to Experience: A Combined EEG and Eye-Tracking Study

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This repository contains the replication package, analysis scripts, and additional information on our study on programmer efficacy and their link to experience.

Our paper was accepted at FSE 2022: Publication: Norman Peitek, Annabelle Bergum, Maurice Rekrut, Jonas Mucke, Matthias Nadig, Chris Parnin, Janet Siegmund, Sven Apel. *Correlates of Programmer Efficacy and Their Link to Experience: A Combined EEG and Eye-Tracking Study*. In Proceedings of the Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE) 2022 ([preprint pdf](https://www.se.cs.uni-saarland.de/publications/docs/PBR+22.pdf)).

---

## Requirements

```
Psychopy
Python 3/ Anaconda
 - Jupyter
 - requirements.txt
Matlab
 - EEGLab
```

## Top Level Structure

### Requirements

The **requirements.txt** provides all the dependencies for the project.
It is recommended to use a separated environment to run the project. One can create suche a virtualenv with the command:

```properties
$ conda create -n your_env_name python=3.8
$ conda activate your_env_name
$ conda install pip
$ pip install -r requirements.txt
```

### Study Preparation

To create the Stimuli the following files where used:
- [SnippetGneration_Lib.py](SnippetGneration_Lib.py)
- [SnippetGneration_JsonGenerators.ipynb](SnippetGneration_JsonGenerators.ipynb)
- [SnippetGneration_ImageGeneration.ipynb](SnippetGneration_ImageGeneration.ipynb)
- [SnippetGneration_ExcelConfig.ipynb](SnippetGneration_ExcelConfig.ipynb)

### Structure

- In [CodeSnippets](CodeSnippets) one can find all Stimuli required by the Study and the Data Evaluation.
- In [Study](Study) one can find the files for running the [PsychoPy](https://www.psychopy.org/) Study.
- In [dataEvaluation](dataEvaluation) one can find the files for running the data evaluation.

---

## Code Snippets

The [CodeSnippets](CodeSnippets) folder contains all the files regarding the Stimuli. The files are the following:
- [Examples](CodeSnippets/Examples) contains the trainings task of the study.
- [fonts](CodeSnippets/fonts) contains the fonts used in the Snippets.
- [Labeled Generators](CodeSnippets/Generators_Labeled) contains the generators for the Labeled Snippets. These are based of Tokens and bigger syntactical structure.
- [Unlabeled Generators](CodeSnippets/Generators_Raw) contains the generators for the simple generating the Images of the Snippets.
- [Snippets](CodeSnippets/Snippets) contains the Snippets as png.
- [Source](CodeSnippets/Source) contains the source code of the Snippets.
- [Syntax](CodeSnippets/Syntax) contains the Syntax tasks for the Study.

---

## Study

The Study folder contains of different file kinds. The files are organized in the following way:
- [Study/libs](Study/libs) are containing the **.whl** files needed for recording Eyetracking and EEG Data in Psychopy. Make Sure to install these **.whl** files to the PsychoPy environment.
- [Study/Resources](Study/Resources) contains images and json files which help to run the study. These are [Distraction Tasks](Study/Resources/DistractionTasks), a [training example](Study/Resources/TrainingExample), a [test example](Study/Resources/Intro), Helpers Images and the [textbase](Study/Resources/textbase.json) for the study. 
- several '*condtion.xlsx' files which are used for finding the stimuli with a relative path. These are also used for the pseudo randomization of the stimuli.
- [Study.psyexp](Study/Study.psyexp) is the main file for running the study.

---

## Data Evaluation

Before you start get the rawData and put it into 'dataEvaluation/data/'

In [Here](dataEvaluation) you will find the files for running the data evaluation. These files are are named from Preporcessing01 to Preporcessing05.
Execute them in order to get the data in the right format. After that you can run the data evaluation of [RQ1](dataEvaluation/RQ1_Eyetracking.ipynb) and [RQ2](dataEvaluation/RQ2_EEG.ipynb).
Make sure to have the EEGLab installed in the [directory](dataEvaluation).

For further Information read the [README.md](dataEvaluation/README.md) of the data evaluation.

# License

This repository is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# Contact

If you have questions, please contact me directly: `peitek@cs.uni-saarland.de`. Thank you!
