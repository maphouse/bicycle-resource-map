let lat;
let lon;
let acc;

let baseLayer = new ol.layer.Tile({
	source: new ol.source.OSM()
});
  
let geojsonLayer = new ol.layer.Vector({
    source: new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: 'http://127.0.0.1:5000/static/data.js'
    }),
    style: new ol.style.Style({
        image: new ol.style.Circle( ({
            radius: 10,
            fill: new ol.style.Fill({
                color: '#000000'
            })
        }))
    })
});


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

let options = {
	enableHighAccuracy: true,
	timeout: 5000,
	maximumAge: 0
};


window.addEventListener('load', function() {
	navigator.geolocation.getCurrentPosition(success, error, options);
});

function renderMap(lat, lon) {
	//map object
	let map = new ol.Map({
		layers: [baseLayer, geojsonLayer],
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