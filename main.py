from flask import Flask
from flask import render_template
import overpass
import json

app = Flask(__name__)

api = overpass.API()
#a more sustainable , modular function is needed to define the area. Right now, the ref id for the Montreal area was retrieved from Overpass xml query in overpass turbo wizard... not sustainable longterm when targeted areaas will be added.
#response2 = api.get('node["shop"="bicycle"](area:3601634158);')
#response3 = api.get('node["amenity"="compressed_air"](area:3601634158);')
#response4 = api.get('node["amenity"="bicycle_parking"](area:3601634158);')
#response5 = api.get('way["amenity"="bicycle_parking"](area:3601634158);')
#'node["amenity"="bicycle_repair_station"](area:3601634158);'
response = api.get('node(area:3601634158)["shop"="bicycle"];')

#url_for('static', filename='style.css')

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/about')
def about():
	return json.dumps(response, indent=4)
@app.route('/contribute')
def contribute():
	return 'this is the contribute page yea'
	

with open('data.js', 'w') as jsonFile:
	json.dump(response, jsonFile, indent=4)