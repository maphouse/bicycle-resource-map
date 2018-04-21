from flask import Flask
import overpass
import json

app = Flask(__name__)

api = overpass.API()
#a more sustainable , modular function is needed to define the area. Right now, the ref id for the Montreal area was retrieved from Overpass xml query in overpass turbo wizard... not sustainable longterm when targeted areaas will be added.
response = api.get('node(area:3601634158)["name"="Chénier"];')
#response2 = api.get('node["shop"="bicycle"](area:3601634158);')
#response3 = api.get('node["amenity"="compressed_air"](area:3601634158);')
#response4 = api.get('node["amenity"="bicycle_parking"](area:3601634158);')
#response5 = api.get('way["amenity"="bicycle_parking"](area:3601634158);')

#'relation["amenity"="bicycle_parking"](area:3601634158);'
#'node["amenity"="bicycle_repair_station"](area:3601634158);'
#'way["amenity"="bicycle_repair_station"](area:3601634158);'
#'relation["amenity"="bicycle_repair_station"](area:3601634158);'

@app.route('/')
def hello_world():
	return json.dumps(response, indent=4)

with open('data.txt', 'w') as jsonFile:
	print("var geojsonData = {")
	json.dump("var geojsonData = {"+ response, jsonFile, indent=4)
