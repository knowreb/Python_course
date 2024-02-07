import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_1m.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Earthquakes around the world in 30 days')

fig ={'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_30.html')