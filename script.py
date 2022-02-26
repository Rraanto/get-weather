import requests
import json
import geocoder

# side function converting kelvin to celcius 
f = lambda k : k - 273.15
# getting location from ip adress : 
location = geocoder.ip('me')
place = str(location[0]).replace("[", "").replace("]", "")

# latitude and longitude of the location
lat, lon = location.latlng[0], location.latlng[1]

# apikey used at openweather (stored in local file only)
container_file = open('./apikey.txt', 'r')
APIKEY = container_file.read().replace("\n", "")

# url used for the http request
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={APIKEY}"

# http request
r = requests.get(url)

# if the request is successful
if int(r.status_code) == 200:
    response = json.loads(r.text)
    main_data = response['current']
    main_weather = main_data['weather'][0]
    print(f"{place}")
    print(f"{main_weather['main']}, {main_weather['description']}")
    print(f"{'Temperature' : <15} : {'%.2f' % f(main_data['feels_like'])}°C")
    print(f"{'Pressure' : <15} : {main_data['pressure']}")
    print(f"{'Humidity' : <15} : {main_data['humidity']}")
else : 
	print(f"Code {r.status_code}")