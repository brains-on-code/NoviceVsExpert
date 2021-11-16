import warnings
from time import sleep

import matplotlib
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import preparers
import os
import regex as re
import sonaion_analysis as son
from pandas.core.common import SettingWithCopyWarning
import GenSnippetsLib as snippet

def lol(numbers):
    print(numbers)
    return 0

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        print("Hello WOrld")
        print(list(executor.map(lol, [1, 2, 3])))