
let lat;
let lon;
let acc;

function success(pos) {
	lat = pos.coords.latitude;
	lon = pos.coords.longitude;
	acc = pos.coords.accuracy;
	renderMap(lat, lon);
	//map.getView().setCenter(ol.proj.fromLonLat([lon, lat]))
}
	
function error(err) {
	console.warn(`ERROR(${err.code}): ${err.message}`);
	renderMap(0,0);
}

var options = {
	enableHighAccuracy: true,
	timeout: 5000,
	maximumAge: 0
};


window.addEventListener('load', function() {
	navigator.geolocation.getCurrentPosition(success, error, options);
});

function loadJSON(callback) {   

    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', 'data.js', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);  
}

function renderMap(lat, lon) {
	//map object
	var map = new ol.Map({
		layers: [
		  new ol.layer.Tile({
			source: new ol.source.OSM()
		  })
		],
		target: 'map',
		controls: ol.control.defaults({
		  attributionOptions: {
			collapsible: false
		  }
		}),
		view: new ol.View({
		  center: ol.proj.fromLonLat([lon, lat]),
		  zoom: 15
		})
	});
}

