import requests

def get_temperature(district):
    # Replace with your API key retrieval method
    with open(".api_key.txt", "r") as file:
        API_KEY = file.read().strip()

    # Construct the API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={district}&appid={API_KEY}"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(response.text)
        raise Exception(f"Unable to get temperature data for {district}")

    # Parse the JSON response
    data = response.json()

    # Extract temperature (in Celsius) from the response
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15  # Convert from Kelvin to Celsius

    return temperature_celsius


def get_temp_hum(district):
    # Replace with your API key retrieval method
    with open(".api_key.txt", "r") as file:
        API_KEY = file.read().strip()

    # Construct the API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={district}&appid={API_KEY}"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(response.text)
        raise Exception(f"Unable to get temperature and humidity data for {district}")

    # Parse the JSON response
    data = response.json()

    # Extract temperature (in Celsius) and humidity from the response
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15  # Convert from Kelvin to Celsius
    humidity = data['main']['humidity']

    return temperature_celsius, humidity
