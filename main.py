import googlemaps
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim, GoogleV3
import requests
import numpy
import gpsd
from utils.AddressCompleter import AddressCompleter



API_KEY = 'AIzaSyDqUQ612HWNtf4_NKSlY_OHhuSaU4uOGGk'
gmaps = googlemaps.Client(key=API_KEY)


# current_location = get_current_add()

if __name__ == "__main__":
    completer = AddressCompleter(API_KEY)
    address = completer.prompt("Current Address: ", completer=completer)
