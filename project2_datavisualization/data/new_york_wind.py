# False error from pyright.
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'new_york_07-2021-2022_wind.csv'

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
# Get station name, dates and wind speeds from this file.
    name, dates, wind_speeds = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
            wind_speed = float(row['AWND'])
            title = row['NAME']
        except ValueError:
            print(f"Missing value at {row}.")
            wind_speed = wind_speeds[-1]
        else: 
            dates.append(current_date)
            name.append(title)
            wind_speeds.append(wind_speed)

# Plot the wind speeds.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, wind_speeds)

# Format the plot.
ax.set_title(f'{name[0]} - ({dates[0]} - {dates[-1]})', fontsize=20)
ax.set_xlabel('Dates(y-m-d)', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Wind speed', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
