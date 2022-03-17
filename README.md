# Correlates of Programmer Efficacy and their Link to Experience

---
## Abstract

**Background:** Despite a similar education and background, programmers can exhibit vast differences in efficacy. While research has identified some potential factors, such as programming experience and domain knowledge, the effect of these factors on programmers' efficacy is not well understood.

**Aims:** We aim at unravelling the relationship between efficacy (speed and correctness) and measures of programming experience. We further investigate the correlates of programmer efficacy in terms of reading behavior and cognitive load.

**Method:** For this purpose, we conducted a controlled experiment with 37 participants using electroencephalography (EEG) and eye tracking. We asked participants to comprehend up to 32 Java source-code snippets and observed their eye gaze and neural correlates of cognitive load. We analyzed the correlation of participants' efficacy with popular programming experience measures.

**Results:** We found that programmers with high efficacy read source code more quickly and accurately and with lower cognitive load. Commonly used experience levels do not predict programmer efficacy well, but self-estimation and indicators of learning eagerness are fairly accurate.

**Implications:** The identified correlates of programmers with high efficacy can be used for future research and practice, such as hiring. Future research should also consider efficacy as a group sampling method, rather than simple experience measures.

---
## Paper

Tba.

---

## Requirements for the Project

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

The **requirements.txt** provides all the Python dependencies for the project.
It is recommended to use a separated environment to run the project. One can create suche a virtualenv with the command:

```properties
$ conda create -n your_env_name python=3.8
$ conda activate your_env_name
$ conda install pip
$ pip install -r requirements.txt
```

### Structure

- In [CodeSnippets](CodeSnippets) are all stimuli used in our study and the data evaluation.
- In [Study](Study) are the files for running the [PsychoPy](https://www.psychopy.org/) study.
- In [dataEvaluation](dataEvaluation) are the files for running the data evaluation.

### Study Preparation

To create our used stimuli, we used the following files:
- [SnippetGneration_Lib.py](SnippetGneration_Lib.py)
- [SnippetGneration_JsonGenerators.ipynb](SnippetGneration_JsonGenerators.ipynb)
- [SnippetGneration_ImageGeneration.ipynb](SnippetGneration_ImageGeneration.ipynb)
- [SnippetGneration_ExcelConfig.ipynb](SnippetGneration_ExcelConfig.ipynb)

---

## Code Snippets

The [CodeSnippets](CodeSnippets) folder contains all the files regarding the stimuli. Specifically, that includes the following:
- [Examples](CodeSnippets/Examples) contains the training tasks of the study.
- [fonts](CodeSnippets/fonts) contains the fonts used in the snippets.
- [Labeled Generators](CodeSnippets/Generators_Labeled) contains the generators for the labeled snippets. These are based of tokens and bigger syntactical structure.
- [Unlabeled Generators](CodeSnippets/Generators_Raw) contains the generators for the simple generating the images of the snippets.
- [Snippets](CodeSnippets/Snippets) contains the snippets as png.
- [Source](CodeSnippets/Source) contains the Java source code of the snippets.
- [Syntax](CodeSnippets/Syntax) contains the syntax tasks for the study.

---

## Study

The study folder contains additional files necessary for running a replication. The files are organized in the following way:
- [Study/libs](Study/libs) are containing the **.whl** files needed for recording eye-tracking and EEG data in PsychoPy. You must install these **.whl** files to the PsychoPy environment.
- [Study/Resources](Study/Resources) contains additional images and json files which are part of the study. These are [distraction tasks](Study/Resources/DistractionTasks), a [training example](Study/Resources/TrainingExample), a [test example](Study/Resources/Intro), helper images and the [textbase](Study/Resources/textbase.json) for the study. 
- Several '*condition.xlsx' files which are used for finding the stimuli with a relative path. These are also used for the pseudo randomization of the stimuli.
- [Study.psyexp](Study/Study.psyexp) is the main file for running the study.

---

## Data Evaluation

Before running the evaluation pipeline, you must obtain the raw data (which will be shared after publication) and move it into 'dataEvaluation/data/'.

In [dataEvaluation](dataEvaluation) you will find the files for running the data evaluation. These files are are named from Preprocessing01 to Preprocessing05.
Execute them in order to obtain the data in the right format. Afterwards, you can run the data evaluation of [RQ1](dataEvaluation/RQ1_Eyetracking.ipynb), [RQ2](dataEvaluation/RQ2_EEG.ipynb), and [RQ3](dataEvaluation/RQ3_ExperienceMeasures.ipynb). You must have EEGLab installed in the [directory](dataEvaluation).

For further information read the [README.md](dataEvaluation/README.md) of the data evaluation or contact as directly.
