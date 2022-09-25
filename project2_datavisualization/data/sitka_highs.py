# False error from pyright.
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])

        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format the plot.
plt.title('Daily high temperatures - 2018', fontsize=24)
plt.xlabel('Dates(y-m-d)', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
