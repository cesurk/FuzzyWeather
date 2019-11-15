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


