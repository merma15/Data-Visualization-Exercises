import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = "data/eq_data_30_day_m1.json"
with open(filename) as file:
    all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title']
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w')  as file:
    json.dump(all_eq_data, file, indent=4)

#map the earthquakes.
#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis', # colorscales
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_erathquakes.html')

