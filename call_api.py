"""Reach out to a free API and return a df of data."""

import requests


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
    data = {
        "stationId": properties["stationId"],
        "stationName": properties["stationName"],
        "timestamp": properties["timestamp"],
        "temp": properties["temperature"]["value"],
        "wind direction": properties["windDirection"]["value"],
        "windSpeed": properties["windSpeed"]["value"],
        "visibility": properties["visibility"]["value"],
        "windGust": properties["windGust"]["value"],
        "rain last 3 hours": properties["precipitationLast3Hours"]["value"],
    }
    return data


if __name__ == "__main__":
    print(parse_weather(get_weather()))
