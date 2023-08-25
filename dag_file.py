from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from weather_data_fetcher import WeatherDataFetcher  # Import the class from your other file
import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'weather_data_dag',
    default_args=default_args,
    schedule_interval='@daily', 
    catchup=False,
)

def fetch_and_store_weather_data():
    api_key = ""#Add API Key 
    cities = ["London", "Paris", "New York", "Tokyo"]

    fetcher = WeatherDataFetcher(api_key)
    weather_data = []

    for city in cities:
        data = fetcher.fetch_data(city)
        if data:
            weather_data.append(data)

    sorted_weather_data = sorted(weather_data, key=lambda x: x["main"]["temp"])

    df = pd.DataFrame(
        [(data["name"], data["main"]["temp"] - 273.15) for data in sorted_weather_data],
        columns=["City", "Temperature (C)"]
    )

    csv_file_name = "s3://airflowbucketgr/test_data/sorted_weather_data.csv"
    df.to_csv(csv_file_name, index=False)

    print(f"Weather data sorted and stored in {csv_file_name}")

fetch_and_store_task = PythonOperator(
    task_id='fetch_and_store_task',
    python_callable=fetch_and_store_weather_data,
    dag=dag,
)

fetch_and_store_task
