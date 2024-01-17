import csv
from datetime import datetime

import matplotlib.pyplot as plt
filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #downloading max and min temp from a file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#generation of a chart of the highest and lowest temperatures from a file
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#chat formatting
ax.set_title("Highest and lowest temperature of day in July - 2018", fontsize=18)

plt.show()