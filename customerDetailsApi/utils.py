import requests
import re
import json
from CustomerDetails.settings import GOOGLE_MAPS_API_KEY


def get_lat_long(address):
    query = re.sub('[^A-Za-z0-9 ]+', '', address)
    query = query.replace(' ', '+')
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GOOGLE_MAPS_API_KEY}')
   
    if response.json()['status'] == 'ZERO_RESULTS':
        return -1, -1    
    
    location =  response.json()['results'][0]['geometry']['location']   
    lat = location['lat']
    lng = location['lng']

    return  lat, lng
    
