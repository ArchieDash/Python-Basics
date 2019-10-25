import os
import csv

wd = 'files/'
with open (os.path.join(wd, 'pastimes.csv'), 'r') as file, open (os.path.join(wd, 'catgorized pastimes.csv'), 'w') as output:
    data = csv.reader(file)
    categorized = csv.writer(output)
    next(data)  # skipping header
    categorized.writerow(['Name','Favotite Pastime','Type of Pastime'])
    for row in data:
        print(row)
        if row[1].lower().find('fighting') != -1:
            row.append('Combat')
        else:
            row.append('Other')
        categorized.writerow(row)
