import requests
import json

def get_data_from_api():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Check the status of the request
    if response.status_code == 200:
        data = response.json()  # Parse response to JSON
        print(json.dumps(data, indent=4))  # Print formatted JSON data
    else:
        print(f"Request failed with status code: {response.status_code}")

get_data_from_api()
