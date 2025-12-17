import call_api
import clean

import pandas as pd


def test_parse_weather():
    packet = {
        "field1": {},
        "field2": {},
        "properties": {
            "stationId": "Xyz",
            "stationName": "Name",
            "timestamp": "2024-01-01T01:23:45Z",
            "temperature": {"field3": "XYZ", "value": 10},
            "windSpeed": {"field4": True, "value": 5},
            "windDirection": {"value": 1},
            "windGust": {"value": 2},
            "visibility": {"value": 3},
            "precipitationLast3Hours": {"value": 1.1},
        },
    }

    result = call_api.parse_weather(packet)

    assert result["station_id"] == "Xyz"
    assert result["year"] == 2024
    assert result["time"] == "01:23:45"
    assert result["temp"] == 10
    assert result["rain_last_3_Hours"] == 1.1


def test_snakecasify_columns():
    d = {"FirstColumn": [0, 1, 2, 3], "2nd Column": [None, None, 2, 3]}
    df = pd.DataFrame(data=d)
    df_s = clean.snakecasify_columns(df)

    print(df_s.head())

    assert df_s.columns.tolist() == ["first_column", "2nd_column"]
