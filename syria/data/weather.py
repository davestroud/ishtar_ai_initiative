import requests
import pandas as pd
import os

# Load the API key from an environment variable
api_key = os.getenv('TOMORROW_IO_API_KEY')

# Ensure the API key is not None
if not api_key:
    raise ValueError(
        "API key not found. Set the TOMORROW_IO_API_KEY environment variable.")

url = 'https://api.tomorrow.io/v4/weather/forecast'

# Parameters for the API request
params = {
    'location': '42.3478,-71.0466',
    'apikey': api_key
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    data = response.json()

    # Temporarily print the keys at the top level of the JSON structure to understand its format
    print(data.keys())

    # Assuming 'data' is a key at the top-level, print keys inside 'data' to further understand the structure
    if 'data' in data:
        print(data['data'].keys())
        if 'timelines' in data['data']:
            # If 'timelines' exists, check its structure
            # Check if it's a list or a dictionary
            print(type(data['data']['timelines']))
            if isinstance(data['data']['timelines'], list) and len(data['data']['timelines']) > 0:
                # Print keys of the first item in 'timelines'
                print(data['data']['timelines'][0].keys())
    # This step is for debugging purposes and helps us correct the DataFrame creation line below
