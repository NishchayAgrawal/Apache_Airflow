# Weather Data Fetcher using Apache Airflow

This project demonstrates how to use Apache Airflow to fetch weather data for multiple cities from an API, sort the data, and store it in a CSV file.

![](https://github.com/Gaurav0807/Apache_Airflow/assets/54076460/a5563b4f-fbe4-491c-9d2d-b3f0a57e2111)


## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [DAG Configuration](#dag-configuration)
- [Contributing](#contributing)

## Prerequisites

- Python 3.x
- AWS Cloud(Used EC2 Instances)
- [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start.html) installed
  


## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/weather-data-fetcher.git
    cd weather-data-fetcher
    ```

2. Install required packages:

    ```bash
    pip install requests pandas apache-airflow
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `"YOUR_API_KEY"` in `weather_data_dag.py` with your actual API key.

## Usage

1. Create EC2 Instance and then install some prerequisites.
   Run commands :-
   ```bash
   sudo apt-get update
   sudo apt install python3-pip
   sudo pip install apache-airflow
   sudo pip install pandas
   sudo pip install requests
   ```

3. Start your Airflow web server:

    ```bash
    airflow standalone
    ```
    Separate window for update code and dag file

    ```bash
    sudo nano weather_data_fetcher.py
    sudo nano dag_file.py
    ```
    
4. Access the Airflow UI in your browser (default: public_address_ec2_instance:8080).
5. Also update IAM Rule for particular instance otherwise it through Error :- Access Denied
   Add IAM Policy :- AmazonS3FullAccess, AmazonEC2FullAccess

6. Trigger the "weather_data_dag" manually or set the desired schedule interval.

## DAG Configuration

In the `weather_data_dag.py` file, you can configure:

- `start_date`: The date from which the DAG starts running.
- `schedule_interval`: The interval at which the DAG is executed (e.g., `'@daily'`).
- `api_key`: Replace with your OpenWeatherMap API key.
- `cities`: Add or modify the list of cities for which you want to fetch weather data.

## Contributing

Contributions are welcome! If you find any issues or improvements, feel free to open a pull request.


