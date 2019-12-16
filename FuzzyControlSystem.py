# Import statements
import requests
from FuzzyMembership import membership
from FuzzyRules import *

# Read in API Keys from txt file into dictionary
def getCredentials():
	# Get credentials from txt file
	with open('API_Keys.txt') as f:
		credentials_array = [x.strip().split(':', 1) for x in f]
	# Translate to dictionary
	credentials = {}
	for cred in credentials_array:
		credentials[cred[0]] = cred[1]
	# Return credentials
	return credentials

# Get Location as input from User
def getLocationFromUser():
	print("Please enter your location using the format: 'City, Country Code'")
	print("For example: 'Kingston, CA'")
	location = str(input("Location: "))
	return location

# Get weather information from OpenWeatherMap API
def getWeather(credentials, location):
	# Build api string
	api_call = (
		"https://api.openweathermap.org/"
		+ "data/2.5/weather?q=" + location.replace(" ", "%20")
		+ "&appid=" + credentials["OpenWeatherAPI"]
		+ "&units=metric" )
	# Execute API call
	response = requests.get(api_call)

	# If API call was not valid, try again
	if (response.status_code != 200):
		print("\nLocation could not be found, please try again!")
		updated_location = getLocationFromUser()
		return getWeather(credentials, updated_location)

	return response.json()

# Apply Fuzzy Rule Set
def applyFuzzyRules(weather):
	# Parse weather data to get wind, temperature, and humidity
	w = weather['wind']['speed']
	t = weather['main']['temp']
	h = weather['main']['humidity']
	# Get and apply membership functions to rules
	wind, temperature, humidity = membership()
	bottom = bottoms(wind, temperature, humidity, w, t, h)
	top = tops(wind, temperature, humidity, w, t, h)
	print("You should wear", bottom, "and a", top,"today.")

# Main function
def main():
	# Get credentials and user's location from input
	credentials = getCredentials()
	location = getLocationFromUser()
	weather = getWeather(credentials, location)
	# Call Fuzzy Rules to decide what to wear!
	applyFuzzyRules(weather)
main()
