from matplotlib import pyplot as plt
import os
import csv


path = os.path.join('files', 'pirates.csv')
years = list()
temps = list()
pirates = list()
with open(path, 'r') as fin:
    data = csv.reader(fin)
    next(data)
    for year, temp, count in data:
        years.append(year)
        temps.append(temp)
        pirates.append(count)
xs = pirates
plt.xlabel('Count pirates')
ys = temps
plt.ylabel('Average temperature')
plt.plot(xs, ys, 'r-o')
plt.title('Quantity relationship of pirates count and year average temperature')
plt.savefig(os.path.join('files', 'pirates.png'))
plt.show()
