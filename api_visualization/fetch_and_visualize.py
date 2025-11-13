import requests
import matplotlib.pyplot as plt
from datetime import datetime
import os
import sys

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Read key from environment
if not API_KEY:
    print("Error: OPENWEATHER_API_KEY environment variable not set.")
    sys.exit(1)

CITY = sys.argv[1] if len(sys.argv) > 1 else 'London'  # Get city from args or default to London

def fetch_weather():
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data.get('cod') != '200':
        raise ValueError(f"API error: {data.get('message', 'Unknown error')}")
    return data

def extract_temperatures(data):
    temps = []
    times = []
    for entry in data['list']:
        temps.append(entry['main']['temp'])
        times.append(datetime.fromtimestamp(entry['dt']))
    return times, temps

def plot_weather(times, temps):
    plt.plot(times, temps, marker='o')
    plt.title(f'Temperature Forecast for {CITY}')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('weather_chart.png')
    plt.show()

def main():
    try:
        data = fetch_weather()
        times, temps = extract_temperatures(data)
        plot_weather(times, temps)
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
