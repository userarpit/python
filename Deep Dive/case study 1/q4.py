import geopy.distance

# Define two points with latitude and longitude
point1 = (52.5200, 13.4050)  # Berlin, Germany
point2 = (48.8566, 2.3522)   # Paris, France

# Calculate the distance between the two points
distance_km = geopy.distance.geodesic(point1, point2).kilometers

# Print the result
print(f"The distance between Berlin and Paris is approximately {distance_km:.2f} kilometers.")
