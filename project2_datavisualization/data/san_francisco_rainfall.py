import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'san_francisco_07-2021-2022.csv'

with open(filename) as f:
    reader = csv.DictReader(f)
    header_column = next(reader)
    for index, header_column in enumerate(header_column):
        print(index, header_column)

    # Get the san francisco annual rainfall amounts and dates.
    dates, rainfall = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
            current_rain = float(row['PRCP'])
        except ValueError:
            print(f"Value is missing at {row}")
        else:
            dates.append(current_date)
            rainfall.append(current_rain)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, rainfall)

ax.set_title('San Francisco annual rainfall', fontsize=24)
ax.set_xlabel('dates', fontsize=14)
ax.set_ylabel('precipitation amount(cubic inches)', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(-0.1, 5)

plt.show()
