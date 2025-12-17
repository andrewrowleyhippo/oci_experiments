"""Take a csv of weather data and parse it."""

import pandas as pd
import re


def snakecasify_columns(df):
    """For a pandas dataframe, coerce column names to snake_case."""

    def to_snake(col):
        col = re.sub(r"[^\w]+", "_", col)
        col = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", col)
        col = col.lower()
        col = re.sub(r"_+", "_", col).strip("_")
        return col

    new_cols = [to_snake(c) for c in df.columns]
    df_s = df.rename(columns=dict(zip(df.columns, new_cols)))
    return df_s


def extract_data_to_df(path):
    df = pd.read_csv(path, header=0)
    return df


def clean_df(df):
    df = snakecasify_columns(df)
    df.drop(["date.month", "date.week_of", "date.year", "station.city"], axis=1)
    return df


if __name__ == "__main__":
    path = "data/weather.csv"
    df = extract_data_to_df(path)
    dfx = clean_df(df)

    print(dfx.head())
