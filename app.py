from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GEOCODE_URL = "https://nominatim.openstreetmap.org/search"
SUN_API_URL = "https://api.sunrise-sunset.org/json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_times', methods=['POST'])
def get_times():
    city = request.form['city']

    # Get latitude & longitude from OpenStreetMap
    geo_params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    geo_response = requests.get(GEOCODE_URL, params=geo_params, headers={"User-Agent": "sunrise-app"})
    geo_data = geo_response.json()

    if not geo_data:
        return render_template('result.html', city=city, error="City not found! Please try again.")

    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # Get sunrise & sunset times
    sun_params = {"lat": lat, "lng": lon, "formatted": 1}
    sun_response = requests.get(SUN_API_URL, params=sun_params)
    sun_data = sun_response.json()

    if sun_data.get('status') != 'OK':
        return render_template('result.html', city=city, error="Could not fetch sunrise/sunset times.")

    sunrise = sun_data['results']['sunrise']
    sunset = sun_data['results']['sunset']

    return render_template('result.html', city=city, sunrise=sunrise, sunset=sunset)

if __name__ == '__main__':
    app.run(debug=True)
