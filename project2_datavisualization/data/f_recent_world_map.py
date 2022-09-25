import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'recent_world_fire_data.csv'

with open(filename) as f:
    reader = csv.DictReader(f)
    header_row = next(reader)

    for index, header_row in enumerate(header_row):
        print(index, header_row)

    longitudes, latitudes, brightnesses, times = [], [], [], []
    for row in reader:
        longitude = str(row['longitude'])
        latitude = str(row['latitude'])
        brightness = float(row['brightness'])
        daynight = row['daynight']
           
        try:
            date = datetime.strptime(row['acq_date'], '%Y-%m-%d')
        except ValueError:
            date = None
        
        time = f'{daynight} of {date} (D means day and N means night)'
        if date == None:
            time = f'Occured at {daynight} (date unknown) (D means day and N'
            time += ' means night)'
        longitudes.append(longitude)
        latitudes.append(latitude)
        brightnesses.append(brightness)
        times.append(time)

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': times,
    'marker': {
        'size': [(mag/100)*5 for mag in brightnesses],
        'color': brightnesses,
        'colorscale': 'Reds',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
        },
    }]

my_layout = Layout(title='World fires in the last seven days')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_data_7_days.html')
