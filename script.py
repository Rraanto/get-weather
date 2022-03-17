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

title = ttk.Label(window, text=place, background="white", font="Helvetica 18 bold")
title.pack()

body = ttk.Frame(window)

temp = ttk.Label(body, background="white", text=f"Temperature : {main_data['feels_like']}K").grid(row=0, column=0)
pres = ttk.Label(body, background="white", text=f"Pressure : {main_data['pressure']}").grid(row=1, column=0)
hum = ttk.Label(body, background="white", text=f"Humidity : {main_data['humidity']}").grid(row=2, column=0)

s.theme_use('clam')


body.pack()
window.mainloop()
