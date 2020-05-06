import requests
import json
import os.path
import sys


class Maps:
    def __init__(self, city):
        self.city = city

    def mapsextract(self):
        """
        Call Google maps API with city/place name
        append and return in two list:
        Coordinates (lattitude, longitude) and address of city/place.
        """
        coordinates = []
        address = []
        i = 0
        url = "https://maps.googleapis.com/maps/api/geocode/json?"
        params = {
            "address": f"{self.city}",
            "key": "AIzaSyB87XtWBnZRETVCp7WIKUEKiIw1WdSSyZQ",
            "language": "fr"
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        completeName = \
            path = os.path.join("ressources/temp/extracted.json")
        f = open(completeName, "w")
        f.write(json.dumps(extracted))
        f.close()
        coordinates.append(extracted['results'][0]['geometry']['location']['lat'])
        coordinates.append(extracted['results'][0]['geometry']['location']['lng'])
        address.append(extracted['results'][0]['formatted_address'])
        return coordinates, address

    def placeextract(self, coordinates):
        """
        Call Google maps API with longitude and lattitude to determine from coordinates which is it.
        Function save in ressources folder the JSON.
        Mainly unfunctional due to distance ranked system from API.
        """
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        params = {
            "type": f"tourist_attraction|point_of_interest",
            # "keyword": f"{splitted}",
            "location": f"{coordinates[0]}, {coordinates[1]}",
            "rankby": "distance",
            # "radius": "1500",
            "key": "AIzaSyB87XtWBnZRETVCp7WIKUEKiIw1WdSSyZQ"
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        completeName = \
            path = os.path.join("ressources/temp/extracted2.json")
        f = open(completeName, "w")
        f.write(json.dumps(extracted))
        f.close()
