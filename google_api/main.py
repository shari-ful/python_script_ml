import os
from dotenv import load_env
import requests


load_env()

API_KEY = os.environ.get('API_KEY')
GOOGLE_MAP_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def get_location_info(address):
    base_url = GOOGLE_MAP_URL
    
    params = {
        'address': address,
        'key': API_KEY
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            formatted_address = data['results'][0]['formatted_address']
            
            print(f'Formatted Address: {formatted_address}')
            print(f'Latitude: {location["lat"]}')
            print(f'Longitude: {location["lng"]}')
        else:
            print(f'Error: {data["status"]}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    address = input("Enter an address: ")
    get_location_info(address)
