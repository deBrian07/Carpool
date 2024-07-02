import gpsd
import numpy
import requests

class Functions():
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