import numpy as np
import pandas as pd
import folium as fo
# import matplotlib.pyplot as plt
map = fo.Map()
x = fo.FeatureGroup(name="My Map")
for lat, lon in ([34,53],[24,-50],[0,0]):
    x.add_child(fo.Marker(location=[lat,lon],popup='hey',icon=fo.Icon(color='red')))
    map.add_child(x)
population = pd.read_csv('volcano.csv')
lat = list(population['Latitude'])
lon = list(population['Longitude'])
name = list(population['V_Name'])

map.show_in_browser()
# plt.sho