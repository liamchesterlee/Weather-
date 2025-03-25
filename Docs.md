# Documentation for WeatherRetriever Script

## Overview

The `WeatherRetriever` script is a simple Python application that retrieves and displays weather information for a specified city using the OpenWeatherMap API. It provides a command-line interface where users can enter a city name to fetch real-time weather details such as temperature, humidity, and weather conditions.

## Dependencies

This script relies on the following Python modules:

- `urllib.request`: Used to make HTTP requests to the OpenWeatherMap API.
- `json`: Used to parse the JSON response from the API.

Ensure you have an active internet connection to fetch weather data.

---

## Class: `WeatherRetriever`

### Description:
This class interacts with the OpenWeatherMap API to fetch weather details for a given city. It includes error handling to manage incorrect inputs, API failures, and connectivity issues.

### Methods:

#### `__init__(self, api_key)`
- **Description:** Initializes an instance of `WeatherRetriever` with an API key.
- **Arguments:**
  - `api_key` (str): The OpenWeatherMap API key required for authentication.

#### `get_weather(self, city_name)`
- **Description:** Fetches and displays weather details for a specified city.
- **Arguments:**
  - `city_name` (str): The name of the city for which weather data is requested.
- **Returns:**
  - `dict`: A dictionary containing weather data if the request is successful.
  - `None`: If the request fails due to an error.
- **Exception Handling:**
  - `urllib.error.HTTPError`: Handles API request errors such as invalid city names.
  - `urllib.error.URLError`: Handles network-related errors.
  - `json.JSONDecodeError`: Handles issues in decoding the API response.
  - `KeyError`: Handles unexpected data format issues.
  - `Exception`: Catches any other unforeseen errors.

---

## Function: `main()`

### Description:
The main function acts as the entry point for the script, allowing users to input a city name and receive weather updates.

### Functionality:
1. Initializes the `WeatherRetriever` class with an API key.
2. Prompts the user for a city name.
3. Calls `get_weather()` to retrieve and display the weather.
4. Allows the user to enter multiple city names until they type `'exit'` to quit.

---

## Usage Instructions

1. **Obtain an API Key**: 
   - Sign up on [OpenWeatherMap](https://openweathermap.org/) to get an API key.

2. **Replace the API Key**: 
   - Update the `API_KEY` variable in the script with your actual API key.

3. **Run the Script**:
   ```sh
   python weather_script.py
   ```
   - Replace `weather_script.py` with the actual script filename.

4. **Enter City Name**:
   - The script prompts:  
     ```
     Enter city name (or type 'exit' to quit):
     ```
   - Enter a valid city name to retrieve weather information.
   - Type `'exit'` to close the program.

---

## Example Output

```
Enter city name (or type 'exit' to quit): New York

Weather Information for New York
Weather: clear sky
Current Temperature: 22.5 °C
Feels Like: 21.8 °C
Humidity: 60 %

Enter city name (or type 'exit' to quit): exit
Exiting program. Goodbye!
```

---

## Error Handling Scenarios

| Error Type                | Cause & Resolution |
|---------------------------|---------------------|
| HTTP Error (400, 404)     | Invalid city name. Check spelling and try again. |
| URL Error                 | No internet connection. Ensure stable network. |
| JSON Decode Error         | API response issue. Retry later. |
| Key Error                 | Unexpected API response format. Check API documentation. |
| General Exception         | Unhandled error. Restart script or check API status. |

---

## Notes
- The script currently uses **metric units** for temperature (°C).
- Modify `units=metric` in the API URL to `units=imperial` for Fahrenheit (°F).
- If the API key is invalid or expired, the request will fail with an HTTP error.

This documentation ensures that users can understand, modify, and troubleshoot the script easily.