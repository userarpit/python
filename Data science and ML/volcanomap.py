import numpy as np
import pandas as pd
import folium as fo
# import matplotlib.pyplot as plt
map = fo.Map()

population = pd.read_csv('csv/volcano.csv')
lat_vol = list(population['Latitude'])
lon_vol = list(population['Longitude'])
name_vol = list(population['V_Name'])

vol = fo.FeatureGroup(name="My volcano Map")

for lat, lon, name in zip(lat_vol,lon_vol,name_vol):
    vol.add_child(fo.Marker(location=[lat,lon],popup=name,icon=fo.Icon(color='red')))
    map.add_child(vol)

vol.add_child(fo.GeoJson(open('world.json',encoding='utf-8-sig').read()))
map.add_child(vol)
map.show_in_browser()
# plt.sho