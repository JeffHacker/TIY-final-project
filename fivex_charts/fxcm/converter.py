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

import pandas as pd
def scatter_to_base64(df, action):
    plt.figure(figsize=(6, 7))
    if action == "ave_pl_by_symbol":
        plt.title("Average Profit/Loss by Currency Pair", fontsize=20)
        mean_df = pd.DataFrame(df.groupby(['symbol']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))
    elif action == "ave_pl_by_wkday":
        plt.title("Average Profit/Loss by Day of the Week", fontsize=18)
        df['dayofweek'] = pd.DatetimeIndex(df['opendatetime']).dayofweek
        mean_df = pd.DataFrame(df.groupby(['dayofweek']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))

    elif action == "ave_pl_by_month":
        df['month'] = pd.DatetimeIndex(df['opendatetime']).month
        plt.title("Average Profit/Loss by Month of the Year", fontsize=18)
        mean_df = pd.DataFrame(df.groupby(['month']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))

    elif action == "ave_pl_by_year":
        df['year'] = pd.DatetimeIndex(df['opendatetime']).year
        plt.title("Average Profit/Loss by Year", fontsize=18)
        mean_df = pd.DataFrame(df.groupby(['year']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))

    elif action == "ave_pl_by_direction":
        plt.title("Average Profit/Loss by Direction of Trade", fontsize=18)
        mean_df = pd.DataFrame(df.groupby(['direction']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))

    elif action == "ave_pl_by_session":
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        plt.title("Average Profit/Loss by Trading Session", fontsize=18)
        mean_df = pd.DataFrame(df.groupby(['session']).grossprofitloss.mean())
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))


    elif action == "ave_pl_by_dir_session":
        plt.title("Average Profit/Loss by Trade Direction per Session", fontsize=14)
        df['hour'] = pd.DatetimeIndex(df['opendatetime']).hour
        df["session"] = df["hour"].map(create_session_range)
        mean_df = pd.pivot_table(df, index=["session", "direction"], values=["grossprofitloss"])
        mean_df['positive'] = mean_df['grossprofitloss'] > 0
        mean_df['grossprofitloss'].plot(kind="bar", color=mean_df.positive.map({True: 'g', False: 'r'}))


#        pivoted_df.plot(kind="bar")
#        df.groupby(['direction']).gross_pl.mean().plot(kind="barh")

    #########################
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')
