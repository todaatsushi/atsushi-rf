# Tube station JSON loading
import os
import pandas as pd


# Open JSON file from dir
# Table source: https://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations
stations = pd.read_json(os.path.join(os.getcwd(), 'home/tube_stations.json'))

# Get Lat, Lng & Name
stations = stations.iloc[:,[2, 4, 5]]
