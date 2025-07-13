import folium

# Create a map object
# You can specify a starting location (latitude, longitude) and zoom level
m = folium.Map(location=[22.725, 75.923], zoom_start=15, tiles="Stamen Toner") # Centered on Seoul

# Save the map to an HTML file
# m.save("my_basic_map.html")

# Add a simple marker
folium.Marker(
    location=[22.725, 75.923],
    popup="<b>Indore</b>",
    tooltip="Click for info",
    icon=folium.Icon(icon="plane", color="orange", icon_color="white")
).add_to(m)

m.save("map_with_markers.html")
