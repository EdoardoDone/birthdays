import csv
from mypackage.birthdays import birthdays

with open('birthdays.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in birthdays.iteritems():
        writer.writerow(row)
