import requests

# Replace with your API key
api_key = "b4bf90dafb34ce2c795299cb74224f94"

# Define the API URL for geocoding
geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q=New%20York&appid={api_key}"

# Send a GET request to the API
response = requests.get(geocode_url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    geocode_data = response.json()
    print(f"Latitude: {geocode_data[0]['lat']}, Longitude: {geocode_data[0]['lon']}")
else:
    print("Failed to retrieve geocoding data", response.status_code)


    ###############################################################################
# Define the API URL
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=New%20York&appid={api_key}"

# Send a GET request to the API
response = requests.get(weather_url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    print(f"Weather in {weather_data['name']}: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp'] - 273.15:.2f}°C")
else:
    print("Failed to retrieve data", response.status_code)