# Imports #
import folium
import requests
import json

# Request para a API #
url = 'http://api.open-notify.org/iss-now.json'
issnow = requests.get(url)
issnow_data = json.loads(issnow.text)
issnow_list = issnow_data["iss_position"]
latitude = issnow_list["latitude"]
longitude = issnow_list["longitude"]

# Fazer o mapa #
mapa = folium.Map(
    location=[latitude, longitude],
    #tiles='Stamen Toner',
    zoom_start=3.5
)

# Adicionar marcador #
folium.Marker(
    location = [latitude, longitude],
    popup='<strong>Estação Espacial</strong><br>Latitude: {}\nLongitude: {}'.format(latitude, longitude),
    tooltip='ISS'
).add_to(mapa)

mapa.save(r'index.html') # Salva a página HTML #
