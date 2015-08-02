import matplotlib.pyplot as plt
from base64 import b64encode
import pandas as pd
import io
import seaborn

def scatter_to_base64(df,action):
    print(df)
    print(df.groupby(['symbol']).gross_pl.mean())
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



    #########################
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')