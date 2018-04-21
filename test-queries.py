import overpass
import json

api = overpass.API()

response = api.get('node(area:3601634158)["shop"="bicycle"];')

#'node["amenity"="compressed_air"](area:3601634158)'
#'node["amenity"="bicycle_repair_station"](area:3601634158)'

with open('data.js', 'w') as jsonFile:
	json.dump(response, jsonFile, indent=4)