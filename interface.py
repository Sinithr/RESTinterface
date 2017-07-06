#!/usr/bin/env python3.4

from flask import Flask, jsonify, request, abort
from math import sqrt

STORES = (
((38.923476, -77.043093), '1827 Adams Mill Rd, DC'),
((38.874674, -77.001121), '1331 4th St, DC'),
((34.046645, -118.259129), '801 S Hope St, LA'),
((33.655242, -117.998635), '21016 Pacific Coast, Huntington Beach'),
((34.143154, -118.131758), 'Shops on Lake Av, Pasadena'),
((34.142889, -118.254599), '252 S Brand Blvd, Glendale'),
((34.097690, -118.330020), '6430 Sunset Blvd, LA'),
((34.017950, -118.493557), '525 Santa Monica Blvd, LA'),
((37.566991, -122.323638), '113 S B St, San Mateo'),
((37.577947, -122.348523), '305 Primrose Rd, Burlingame'),
((37.775523, -122.393391), '201 Berry St, SF'),
((37.760096, -122.434625), '549 Castro St, SF'),
((37.782402, -122.420482), '748 Van Ness Ave, SF'),
((37.788778, -122.393232), '300 Folsom St, SF')
)

app = Flask(__name__)

### searching stores around location with input radius
@app.route('/interface', methods=['PUT'])
def search():
    global STORES

    # checking request
    if not request.json or not 'location' in request.json:
        abort(400)

    # converting input data
    if 'km_radius' in request.json:
        km_radius = request.json['km_radius']
    else:
        km_radius = 10.
    location = request.json['location']

    # finding shops around location
    shops = []
    for store in STORES:
        if distance(store[0], location) <= float(km_radius):
            shop = [distance(store[0], location), store[1]]
            shops.append(shop)

    # sorting 
    shops = sorted(shops, key=lambda k: k[0])

    return jsonify(shops)

def distance(locationA, locationB): # distance between 2 points
    return sqrt((locationA[0]-locationB[0])**2 + (locationA[1]-locationB[1])**2)

if __name__ == '__main__':
    app.run(debug=True)
