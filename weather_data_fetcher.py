import requests
import csv
import pandas as pd
import s3fs


class WeatherDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    def fetch_data(self, city_name):
        response = requests.get(self.api_url.format(city_name=city_name, api_key=self.api_key))
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data for {city_name}. Status code: {response.status_code}")
            return None

if __name__ == "__main__":
    # api_key = "bab35a7d8848a283f4bafbbb86fb13ca"  
    # cities = ["London", "Paris", "New York", "Tokyo"]  
    # fetcher = WeatherDataFetcher(api_key)
    # weather_data = []

    # for city in cities:
    #     data = fetcher.fetch_data(city)
    #     if data:
    #         weather_data.append(data)

    # print(weather_data)

    # sorted_weather_data = sorted(weather_data, key=lambda x: x["main"]["temp"])


    # df = pd.DataFrame(
    #     [(data["name"], data["main"]["temp"] - 273.15) for data in sorted_weather_data],
    #     columns=["City", "Temperature (C)"]
    # )

    # csv_file_name = "sorted_weather_data.csv"
    # df.to_csv(csv_file_name, index=False)

    # print(f"Weather data sorted and stored in {csv_file_name}")
