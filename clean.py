'''Take a csv of weather data and parse it.'''


import pandas as pd

def snakecasify_columns(df):
    '''For a pandas dataframe, coerce column names to snake_case.'''
    cols = df.columns.tolist()
    cols_mod = [0]*len(cols)
    for i, c in enumerate(cols):
        cols_mod[i] = c.lower().strip().replace(" ","_")
    d = dict(zip(cols, cols_mod))
    df.rename(columns=d, inplace=True)
    return df


def extract_data_to_df(path):
    df = pd.read_csv(path, header = 0)
    return df


def clean_df(df):
    df = snakecasify_columns(df)
    df.drop([
        'date.month',
        'date.week_of',
        'date.year',
        'station.city'
        ], axis=1)
    return df


if __name__ == "__main__":
    path = 'data/weather.csv'
    df = extract_data_to_df(path)
    clean_df(df)