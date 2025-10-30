import folium

# Create a map centered on a location (San Francisco in this example)
m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Add a marker
folium.Marker(
    location=[37.7749, -122.4194],
    popup="Hello, Folium!",
    tooltip="Click me!"
).add_to(m)

# Save the map to an HTML file
m.save("map.html")
print("Map created successfully! Open map.html in your browser to view it.")
