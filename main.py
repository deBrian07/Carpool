import googlemaps
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim, GoogleV3
import requests
import numpy
import gpsd
from utils.AddressCompleter import AddressCompleter
from utils.Functions import Functions



API_KEY = 'AIzaSyDqUQ612HWNtf4_NKSlY_OHhuSaU4uOGGk'
gmaps = googlemaps.Client(key=API_KEY)


# current_location = get_current_add()

if __name__ == "__main__":
    completer = AddressCompleter(API_KEY)
    functions = Functions(API_KEY)

    # input
    address = completer.prompt("Current Address: ", completer=completer)

    num_stops = int(input('How many stops: '))
    stops = []
    for i in range(num_stops):
        temp = completer.prompt(f"Address {i+1}: ", completer=completer)
        stops.append(temp)
    # print(functions.calc_total_duration(address, stops))

    # try different combs
    possibilities = functions.all_combinations(stops) # finds all possible conbinations of the list
    fastest_min = 0
    fastest_comb = 0

    for i in range (len(possibilities)):
        mins = functions.calc_total_duration(address, possibilities[i])
        if fastest_min == 0 or mins < fastest_min:
            fastest_min = mins
            fastest_comb = i
    
    for i in range(len(possibilities[fastest_comb])):
        print(i, possibilities[fastest_comb][i])
    