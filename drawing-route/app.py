import folium
from folium import PolyLine


initial_map = folium.Map(location=[-6.3728253, 34.8924826], zoom_start=5)

routes = [
    (-5.0889, 39.1023), (-6.7924, 39.2083), (-6.8278, 37.6591)
]

PolyLine(routes, color='green', weight=10,
         opacity=0.5).add_to(initial_map)

initial_map.save('index.html')
