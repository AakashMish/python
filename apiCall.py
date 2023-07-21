import requests
import json

def get_and_parse_api_response(api_url):
    try:
        # Make the API call
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            for element in data:
                print('Print element data here')
        else:
            print(f"Error while calling API. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")

if __name__ == "__main__":
    api_url = 'https://abc.com/element' # replace with actual URL
    get_and_parse_api_response(api_url)
