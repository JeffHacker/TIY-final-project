import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn
from base64 import b64encode
from django_pandas.io import read_frame



def create_session_range(hour):
    if 3 <= hour < 8:
        return "Eur"
    elif 8 <= hour < 17:
        return "US"
    else:
        return "Asia"


def scatter_to_base64(df, action):
    if action == "ave_pl_by_symbol":
        image = df.groupby(['symbol']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_wkday":
        df['dayofweek'] = pd.DatetimeIndex(df['opendatetime']).dayofweek
        image = df.groupby(df['dayofweek']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_month":
        df['month'] = pd.DatetimeIndex(df['opendatetime']).month
        image = df.groupby(df['month']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_year":
        df['year'] = pd.DatetimeIndex(df['opendatetime']).year
        image = df.groupby(df['year']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_direction":
        image = df.groupby(['direction']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_session":
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        image = df.groupby(df['session']).grossprofitloss.mean().plot(kind="barh")
    elif action == "ave_pl_by_dir_session":
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        pivoted_df = pd.pivot_table(df, index=["session", "direction"], values=["grossprofitloss"])
        image = pivoted_df.plot(kind="barh")

    #########################
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')
