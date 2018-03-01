# import csv module
import csv

filename = "Scan 12225 toluene and pxylene.csv"

# initialising the titles and rows list
fields = []
cols = []
rows = []

with open(filename, 'r') as datafile:
    # interesting, I've never created an object like this
    csvreader = csv.reader(datafile, delimiter = ' ', quotechar = ':')

    fields = csvreader.next()

    for col in csvreader:
        cols.append(col)
    for row in csvreader:
        rows.append(row)

# printing field names
# print(fields)
print('rows: %10s', rows[:5])
print('columns: %10s', cols[:5])

# for col in cols[:5]:
#    for row in col:
#        print('%10s'%col),
#        print('\n')
  
for col in cols:
    for row in col:
        if 'toluene' in row:
            print(col)
