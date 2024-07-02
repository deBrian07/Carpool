import gpsd
import numpy
import requests
import googlemaps
import itertools

class Functions():
    def __init__(self, api_key=''):
        self.gmaps = googlemaps.Client(key=api_key)

    def get_current_add(self):
        # getting current coor
        # response = requests.get('https://ipinfo.io/')
        # data = response.json()
        # location = data['loc'].split(',')
        # lat = numpy.float16(location[0])
        # lon = numpy.float16(location[1])

        gpsd.connect()
        packet = gpsd.get_current()
        lat = numpy.float16(packet.lat)
        lon = numpy.float16(packet.lon)


        # getting address
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        address = data['results'][0]['formatted_address']
        return address
    
    def calc_total_duration(self, start='', stops=[]):
        sum_dur = 0
        for i in range(len(stops)):
            if i == 0:
                dis_matrix = self.gmaps.distance_matrix(start, stops[0])
                sum_dur += dis_matrix['rows'][0]['elements'][0]['duration']['value']
            elif i+1 < len(stops):
                dis_matrix = self.gmaps.distance_matrix(stops[i], stops[i+1])
                sum_dur += dis_matrix['rows'][0]['elements'][0]['duration']['value']

        return sum_dur
    
    def all_combinations(self, array):
        permutations = list(itertools.permutations(array))
        return permutations