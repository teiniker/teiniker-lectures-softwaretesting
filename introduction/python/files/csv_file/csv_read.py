import csv

with open('data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        print('line: {} data: {}'.format(row[0], row[1]))


