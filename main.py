from flask import Flask, render_template, request, redirect, Response
import overpass
import json
import time
import sys

app = Flask(__name__)
#allows u to run file using python command
if __name__ == "__main__":
	app.run(debug=True, port=5000)

timeThen = 0

def fetchData():
	#a more sustainable , modular function is needed to define the area. Right now, the ref id for the Montreal area was retrieved from Overpass xml query in overpass turbo wizard... not sustainable longterm when targeted areaas will be added.
	#response2 = api.get('node["shop"="bicycle"](area:3601634158);')
	#response3 = api.get('node["amenity"="compressed_air"](area:3601634158);')
	#response4 = api.get('node["amenity"="bicycle_parking"](area:3601634158);')
	#response5 = api.get('way["amenity"="bicycle_parking"](area:3601634158);')
	#'node["amenity"="bicycle_repair_station"](area:3601634158);'
	#'node(45.415077,-74.070401,45.677474,-73.393472)["shop"="bicycle"];
	api = overpass.API(timeout=180)
	response = api.get('(node["shop"="bicycle"];node["amenity"="bicycle_repair_station"];node["amenity"="compressed_air"];)')

	with open('static/data.js', 'w') as jsonFile:
		json.dump(response, jsonFile, indent=4)
def timeCheck(t):
	if (t - timeThen) >= 86400:
		fetchData()
		global timeThen
		timeThen = t
		return timeThen
	else:
		pass


@app.route('/', methods=['POST','GET'])
def index():
	timeNow = time.time()
	timeCheck(timeNow)
	#return 'It has been ' + str(timeNow - timeThen) + ' since last data update. Has data has been updated?'
	return render_template('index.html')
@app.route('/position', methods=['POST','GET'])
def pos():
	data = request.get_json()
	return "data is " + format(data)
	#return json.dumps(data, indent=4)
@app.route('/about')
def about():
	return json.dumps(response, indent=4)
@app.route('/contribute')
def contribute():
	lat = request.args.get('lat')#if key doesn't exist, returns None
	lon = request.args.get('lon')#if key doesn't exist, returns None
	return '<h1>The lat is: {} and lon is: {}</h1>'.format(lat, lon)
@app.route('/test', methods=['POST','GET'])
def test():
	t1 = time.time()
	return str(time.time())
