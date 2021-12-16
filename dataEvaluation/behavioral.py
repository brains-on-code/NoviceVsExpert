import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import preparers
import seaborn as sns
import json
import os
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

def extract_time(behavioral_data, participant, kind="Snippet"):
    columns = ["Participant", "Duration"]
    start = behavioral_data[kind + "Start"][0]
    end = behavioral_data[kind + "Stop"][0]
    df_tmp = pd.DataFrame([[participant, end - start]], columns=columns)
    df_tmp = df_tmp.set_index("Participant")
    return df_tmp


def extract_response(behavioral_data, participant):
    columns = ["Participant", "Response"]
    answer = behavioral_data["ChoosenAnwer"][0]
    df_tmp = pd.DataFrame([[participant, answer]], columns=columns)
    df_tmp = df_tmp.set_index("Participant")
    return df_tmp


def get_behavioral_df(participants):
    df_total = None
    for participant in participants:
        snippets = []
        with open("./filteredData/Participant{}/DataBase.json".format(str(participant).zfill(2)), "r") as f:
            data = json.load(f)
            for snippet_name in data:
                snippets.append(snippet_name)

                data = preparers.load_queried(
                    participant_number=participant, snippets=[snippets], query_behavioral=True
                )

                data = pd.read_excel(data[snippet_name]["Behavioral"])
                df_behaviroal = extract_time(data, participant, kind="Snippet")
                df_behaviroal = df_behaviroal.join(extract_response(data, participant), how="outer")
                df_behaviroal["Snippet"] = snippet_name
                df_total = df_total.append(df_behaviroal) if df_total is not None else df_behaviroal
    return df_total