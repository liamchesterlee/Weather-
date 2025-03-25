import urllib.request
import json

class WeatherRetriever:
    """
    A class to retrieve weather information for a given city using OpenWeatherMap API.
    
    This class provides a method to fetch current weather details 
    with error handling and informative output.
    """
    
    def __init__(self, api_key):
        """
        Initialize the WeatherRetriever with an API key.
        
        Args:
            api_key (str): OpenWeatherMap API key for authentication
        """
        self.API_key = api_key
    
    def get_weather(self, city_name):
        """
        Retrieve and display weather information for a specified city.
        
        Args:
            city_name (str): Name of the city to get weather for
        
        Returns:
            dict: Weather information if successful, None otherwise
        """
        try:
            # Construct the API URL with city name and API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.API_key}&units=metric"
            
            # Open URL and read response
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())
            
            # Print weather information
            print(f"\nWeather Information for {city_name}")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Current Temperature: {data['main']['temp']} °C")
            print(f"Feels Like: {data['main']['feels_like']} °C")
            print(f"Humidity: {data['main']['humidity']} %")
            
            return data
        
        except urllib.error.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
            print("Please check the city name or your internet connection.")
        
        except urllib.error.URLError as url_err:
            print(f"URL Error occurred: {url_err}")
            print("Please check your internet connection.")
        
        except json.JSONDecodeError as json_err:
            print(f"JSON Decoding Error: {json_err}")
            print("There was an issue processing the weather data.")
        
        except KeyError as key_err:
            print(f"Key Error: {key_err}")
            print("Unexpected data format from the weather service.")
        
        except Exception as err:
            print(f"Unexpected error occurred: {err}")
        
        return None

def main():
    """
    Main function to run the weather retrieval program.
    """
    # Replace with your actual OpenWeatherMap API key
    API_KEY = "64af933dcc5a185f6f9e49566ac4e49b"
    
    # Create an instance of WeatherRetriever
    weather_app = WeatherRetriever(API_KEY)
    
    while True:
        # Prompt for city name
        city_name = input("Enter city name (or type 'exit' to quit): ")
        
        # Check for exit condition
        if city_name.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        
        # Retrieve and display weather
        weather_app.get_weather(city_name)

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()