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
    plt.figure(figsize=(6, 6))
    if action == "ave_pl_by_symbol":
        plt.title("Average Profit/Loss by Currency Pair", fontsize=20)
        image = df.groupby(['symbol']).grossprofitloss.mean().plot(kind="bar")#,
                                                                   #color=df.positive.map({True: 'r', False: 'g'}))
        # plt.ylabel("Difference between Heads & Tails")
        # plt.xlabel("2**x flips")

    elif action == "ave_pl_by_wkday":
        df['dayofweek'] = pd.DatetimeIndex(df['opendatetime']).dayofweek
        plt.title("Average Profit/Loss by Day of the Week", fontsize=18)
        image = df.groupby(df['dayofweek']).grossprofitloss.mean().plot(kind="bar", color='red')

    elif action == "ave_pl_by_month":
        df['month'] = pd.DatetimeIndex(df['opendatetime']).month
        plt.title("Average Profit/Loss by Month of the Year", fontsize=18)
        image = df.groupby(df['month']).grossprofitloss.mean().plot(kind="bar")

    elif action == "ave_pl_by_year":
        df['year'] = pd.DatetimeIndex(df['opendatetime']).year
        plt.title("Average Profit/Loss by Year", fontsize=18)
        image = df.groupby(df['year']).grossprofitloss.mean().plot(kind="bar")

    elif action == "ave_pl_by_direction":
        plt.title("Average Profit/Loss by Direction of Trade", fontsize=18)
        image = df.groupby(['direction']).grossprofitloss.mean().plot(kind="bar")

    elif action == "ave_pl_by_session":
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        plt.title("Average Profit/Loss by Trading Session", fontsize=18)
        image = df.groupby(df['session']).grossprofitloss.mean().plot(kind="bar")

    elif action == "ave_pl_by_dir_session":
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        pivoted_df = pd.pivot_table(df, index=["session", "direction"], values=["grossprofitloss"])
        plt.title("Average Profit/Loss by Trade Direction per Session", fontsize=16)
        image = pivoted_df.plot(kind="bar")

    #########################
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')
