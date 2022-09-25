# False error from pyright.
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'death_valley_2018_simple.csv'

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
# Get station name, dates, and high and low temperatures from this file.
    name, dates, highs, lows = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        try:
            f_high = int(row['TMAX'])
            f_low = int(row['TMIN'])
            title = row['NAME']
        except ValueError:
            print(f"Missing value at {row}.")
        else:
            high = float((f_high-32) * 5/9)
            low = float((f_low-32) * 5/9)
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            name.append(title)

# Plot the high and low temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, label='Maximum Temperatures')
ax.plot(dates, lows, c='blue', alpha=0.5, label='Lowest Temperatures')
ax.legend(loc='upper left')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
ax.set_title(f'{name[0]} - ({dates[0]} - {dates[-1]})', fontsize=20)
ax.set_xlabel('Dates(y-m-d)', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(-4.8, 54)

plt.show()
