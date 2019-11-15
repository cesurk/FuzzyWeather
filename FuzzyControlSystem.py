# Import statements
import requests

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

# Get weather information from OpenWeatherMap API
def getWeather(credentials, location):
	# Build api string
	api_call = (
		"https://api.openweathermap.org/" 
		+ "data/2.5/weather?q=" + location.replace(" ", "+")
		+ "&appid=" + credentials["OpenWeatherAPI"] )
	# Make api call
	response = requests.get(api_call)
	print(response)
	return response

# Apply Fuzzy Rule Set
def applyFuzzyRules():
	return

# Main function
def main():
	# Get credentials and user's location from input
	credentials = getCredentials()
	location = str(input("Enter your location: "))
	# Get weather for current location
	weather = getWeather(credentials, location)
	# Call Fuzzy Rules to decide what to wear!
	applyFuzzyRules()

main()