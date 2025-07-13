import numpy as np
import pandas as pd
import folium as fo

map = fo.Map()
population = pd.read_csv('csv/uscities.csv')
lat_vol = list(population['lat'])
lon_vol = list(population['lng'])
name_vol = list(population['city'])
population_vol = list(population['population'])

def mar(popul):
    if popul < 3500000:
        return 'red'
    elif popul >= 3500000 and popul < 6000000:
        return 'blue'
    else:
        return 'pink'
    
vol = fo.FeatureGroup(name="US Cities Map")
for lat, lon, name, popul in zip(lat_vol, lon_vol, name_vol, population_vol):
    vol.add_child(fo.Marker(location=[lat,lon],popup=[name,popul],icon=fo.Icon(color=mar(popul))))
    map.add_child(vol)

map.show_in_browser()