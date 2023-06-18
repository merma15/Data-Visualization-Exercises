import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    #get dates, and high and low temperatures from this rule.
    dates, highs, lows, rains = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low = int(row[5])
            high = int(row[4])
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
            rains.append(rain)
    #plot the data
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #ax.plot(dates, highs, c='grey', alpha=0.5)
    #ax.plot(dates, lows, c='pink', alpha=0.5)
    #ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)
    ax.plot(dates, rains, c='blue')

    #Format plot.
    title = "Daily high and low temperatures - 28\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperatures (F)',fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)


    for index, column_header in enumerate(header_row):
        print(index, column_header)


plt.show()