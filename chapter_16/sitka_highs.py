import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #downloading maximum temperatures from a file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#chart data
plt.style.use('grayscale')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue')

#chart formatting
ax.set_title("Highest temperature of the day - July 2018", fontsize=18)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()