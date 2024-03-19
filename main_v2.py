import requests
import pandas as pd

# The API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Show the DataFrame
    print(df.head())  # Print the first few rows of the DataFrame
else:
    print("Failed to retrieve data. Status code:", response.status_code)
