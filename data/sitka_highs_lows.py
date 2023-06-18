import csv
from datetime import datetime
import matplotlib.pyplot as plt

#filename = "data/sitka_weather_07_2018_simple.csv"
filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    #get dates and high temperatures from this file.
    dates, highs, lows, rains = [], [], [], []
    for row in reader:
        low = int(row[6])
        high = int(row[5])
        rain = float(row[3])
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        rains.append(rain)

    #print(highs)
    #print(dates)
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    #plot the high and low temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #ax.plot(dates, highs, c='red', alpha=0.5)
    #ax.plot(dates, lows, c="grey", alpha=0.5)
    #plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
    ax.plot(dates, rains, c="green", alpha=0.5)

    #format plot.
    #plt.title("Dily high temperatures, july 2018", fontsize=24)
    plt.title("Dily high and low temperatures - 2018", fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate() #draws the labels diagonally to prevent them from overlapping.
    plt.ylabel('Temperature (F)',fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()