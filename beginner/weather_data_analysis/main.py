import json
import os
from datetime import datetime

def load_weather_data():
    """
    Load weather data from a JSON file.
    Returns: (list): A list of weather records.
    """
    file_path = os.path.join("beginner", "weather_data_analysis", "data", "weather.json")
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Corrupt weather.json, starting fresh.")
        return []

def save_weather_data(data):
    """
    Save weather data to a JSON file.
    Args: data (list): List of weather records to be saved.
    """
    file_path = os.path.join("beginner", "weather_data_analysis", "data", "weather.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def compute_average(values):
    """
    Compute the average of a list of numerical values.
    Args: values (list): A list of numbers.
    Returns: float: The average of the values. Returns 0 if the list is empty.
    """
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    return total / count if count != 0 else 0

def analyze_weather(data):
    """
    Analyze and display summary for the given weather data.
    Args: data (list): List of weather records (dicts) containing temperature, humidity, wind speed, and precipitation.
    """
    temperatures = [entry['temperature'] for entry in data]
    humidities = [entry['humidity'] for entry in data]
    wind_speeds = [entry['wind_speed'] for entry in data]
    precipitations = [entry['precipitation'] for entry in data]

    print("\nWeather Data Summary")
    print(f"Total Records: {len(data)}")
    print(f"Average Temperature: {compute_average(temperatures):.2f} °C")
    print(f"Max Temperature: {max(temperatures)} °C")
    print(f"Min Temperature: {min(temperatures)} °C")
    print(f"Average Humidity: {compute_average(humidities):.2f}%")
    print(f"Average Wind Speed: {compute_average(wind_speeds):.2f} km/h")
    
    rainy_days = 0
    for p in precipitations:
        if p > 0:
            rainy_days += 1
    print(f"Rainy Days: {rainy_days}")

def add_new_weather_entry():
    """
    Collect weather data from user input and append it to the data file.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Adding new weather data for today: {today}")

    try:
        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        wind_speed = float(input("Enter wind speed (km/h): "))
        precipitation = float(input("Enter precipitation (mm): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.\n")
        return  # ❗ Important fix: Stop here if input is invalid

    data = load_weather_data()
    data.append({
        "date": today,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "precipitation": precipitation
    })
    save_weather_data(data)
    print("New entry added successfully!\n")

def run_analysis():
    """
    Load weather data and print analysis summary.
    """
    try:
        data = load_weather_data()
        if not data:
            print("No weather data available.\n")
            return
        analyze_weather(data)
    except Exception as e:
        print(f"Error: {e}")

def show_menu():
    """
    Display the main menu options to the user.
    """
    print("Weather Analyzer")
    print("1. View Weather Summary")
    print("2. Add New Weather Entry")
    print("3. Exit")

def main():
    """
    Main loop that runs the Weather Analyzer CLI.
    """
    flag = True
    while flag:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            run_analysis()
        elif choice == '2':
            add_new_weather_entry()
        elif choice == '3':
            print("Exit successful.")
            flag = False
        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()