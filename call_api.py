"""Reach out to a free API and return a df of data."""

import requests
from datetime import datetime, timezone


def get_stations():
    weather_api = "https://api.weather.gov/stations"
    x = requests.get(weather_api).json()
    return x["features"]


def get_weather(station_id="0516W"):
    """Default New York Station"""
    weather_api = f"https://api.weather.gov/stations/{station_id}/observations/latest"
    x = requests.get(weather_api).json()
    return x


def parse_weather(packet):
    properties = packet["properties"]
    dt = datetime.strptime(properties["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
    data = {
        "station_id": properties["stationId"],
        "station_name": properties["stationName"],
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "time": dt.strftime("%H:%M:%S"),
        "temp": properties["temperature"]["value"],
        "wind_direction": properties["windDirection"]["value"],
        "wind_speed": properties["windSpeed"]["value"],
        "visibility": properties["visibility"]["value"],
        "wind_gust": properties["windGust"]["value"],
        "rain_last_3_Hours": properties["precipitationLast3Hours"]["value"],
    }
    return data


if __name__ == "__main__":
    print(parse_weather(get_weather()))
