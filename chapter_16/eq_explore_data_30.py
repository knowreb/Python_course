import json

# data structure analysis
filename = 'data/eq_data_30_day_1m.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts=all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


