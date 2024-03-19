import requests
import pandas as pd

# Your API URL
url = "https://api.unhcr.org/population/v1/idmc/?page=56&limit=56&yearFrom=56&yearTo=56&year=&download=true&coo=coo_example&coa=coa_example&coo_all=true&coa_all=true&cf_type=cfType_example"
# Set the headers
headers = {
    "Accept": "application/json"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a pandas DataFrame
    data = response.json()
    df = pd.json_normalize(data)

    # If the data is deeply nested, you might need to normalize it further
    # For example:
    # df = pd.json_normalize(data, record_path=['path_to_data'])

    print(df)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
