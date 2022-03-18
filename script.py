import requests
import json
import geocoder
import tkinter as tk
from tkinter import ttk


# side function converting kelvin to celcius
def f(k):
    return k - 273.15


# getting location from ip adress 
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
else:
    print(f"Code {r.status_code}")

# tkinter window
window = tk.Tk()
window.geometry("512x256")

s = ttk.Style()
s.theme_use('clam')

title = ttk.Label(window, text=place, background="white", font="Helvetica 20 bold")
title.pack()

main_weather_description = ttk.Label(
    window,
    background="white",
    text=f"{main_weather['main'].capitalize()}, {main_weather['description']}",
    font="Helvetica 18 bold"
)
main_weather_description.pack()

temp = ttk.Label(
    window,
    background="white",
    text=f"Temperature : {main_data['feels_like']}K",
    font="Helvetica 16"
)
pres = ttk.Label(
    window,
    background="white",
    text=f"Pressure : {main_data['pressure']}",
    font="Helvetica 16"
)
hum = ttk.Label(
    window,
    background="white",
    text=f"Humidity : {main_data['humidity']}",
    font="Helvetica 16"
)

temp.pack(ipady=6, ipadx=6, anchor="w")
pres.pack(ipady=6, ipadx=6,anchor="w")
hum.pack(ipady=6, ipadx=6, anchor="w")

s.theme_use('clam')

window.mainloop()
