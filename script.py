import requests
import json
import geocode

# side function turning kelvin to celcius 
f = lambda k : k - 273.15

# getting location from IP adress : 
location = geocode.ip('me')
place = location[0].replace("[", "").replace("]", "")


# latitude and longitude of the place
lat, lon = location.latlng[0], location.latlng[1]

# apikey used at openweather
APIKEY = "" #PUT YOUR API KEY IN THIS VARIABLE

# url used for the http request
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={APIKEY}"

# http request
r = requests.get(url)

# if the request is successful
if int(r.status_code) == 200:
    response = json.loads(r.text)
    main_data = response['current']
    main_weather = main_data['weather'][0]
    print(f"""Weather in {place} : 
{main_weather['main']}, {main_weather['description']};
temperature : {"%.2f" % f(main_data['feels_like'])}°C,
pressure 	: {main_data['pressure']},
humidity 	: {main_data['humidity']}	
""")
else : 
	print(f"Code {r.status_code}")