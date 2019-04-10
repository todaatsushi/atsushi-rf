# Tube station JSON loading
import os
import pandas as pd

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
