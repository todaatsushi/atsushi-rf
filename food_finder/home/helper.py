# Tube station JSON loading
import os
import pandas as pd
import json as j

# Zomato API configure
from pyzomato import Pyzomato
from secret import ZOMATO_API_KEY

# Initialise Zomato Object
zomato = Pyzomato(ZOMATO_API_KEY)


# Open JSON file from dir
# Table source: https://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations
stations = pd.read_json(os.path.join(os.getcwd(), 'home/tube_stations.json'))

# Get Lat, Lng & Name
stations = stations.iloc[:,[2, 4, 5]]


# Get categories
categories = zomato.getCategories()
categories = [
    [r['categories']['id'], 
     r['categories']['name']] 
     
     for r in categories['categories']

     if r['categories']['name'] in 
     ['Cafes', 'Breakfast', 'Lunch', 
      'Dinner', 'Pubs & Bars', 'Clubs & Lounges']
     ]


# VueJs json files
# Categories as json
categories_json = {}
for i in range(0, len(categories)):
    categories_json[categories[i][1]] = categories[i][0]

categories_json = j.dumps(categories_json, ensure_ascii=True)


# Stations as json
stations_json = {}
for i in range(0, len(stations.index)):
    stations_json[stations.iloc[i, 2]] = { 'lat': stations.iloc[i, 0], 'lon': stations.iloc[i, 1]}

stations_json = j.dumps(stations_json, ensure_ascii=True)


# Station names array
station_names = []
for i in range(0, len(stations.index)):
    stop = stations.iloc[i, 2]
    if stop not in station_names:
        station_names.append(stop)


station_names = j.dumps(station_names, ensure_ascii=True)