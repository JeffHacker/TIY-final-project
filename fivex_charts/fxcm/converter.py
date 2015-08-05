import matplotlib.pyplot as plt
from base64 import b64encode
import pandas as pd
import io
import seaborn

def scatter_to_base64(df,action):
    if action == "ave_pl_by_symbol":
        image = df.groupby(['symbol']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_wkday":
        df['dayofweek'] = pd.DatetimeIndex(df['open_date']).dayofweek
        image = df.groupby(df['dayofweek']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_month":
        df['month'] = pd.DatetimeIndex(df['open_date']).month
        image = df.groupby(df['month']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_year":
        df['year'] = pd.DatetimeIndex(df['open_date']).year
        image = df.groupby(df['year']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_direction":
        image = df.groupby(['direction']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_session":
        df['hour'] = pd.DatetimeIndex(df['open_date']).hour
        def create_session_range(hour):
            if 3 <= hour < 8:
                return "Eur"
            elif 8 <= hour < 17:
                return "US"
            else:
                return "Asia"
        df["session"] = df["hour"].map(create_session_range)
        image = df.groupby(df['session']).gross_pl.mean().plot(kind="barh")
    elif action == "ave_pl_by_dir_session":
        df['hour'] = pd.DatetimeIndex(df['open_date']).hour
        def create_session_range(hour):
            if 3 <= hour < 8:
                return "Eur"
            elif 8 <= hour < 17:
                return "US"
            else:
                return "Asia"
        df["session"] = df["hour"].map(create_session_range)
        pivoted_df = pd.pivot_table(df, index=["session", "direction"], values=["gross_pl"])
        image = pivoted_df.plot(kind="barh")


    #########################
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')