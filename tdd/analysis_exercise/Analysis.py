import csv
import statistics

# read a CSV file into a list of lists
with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    data = list(reader)
    print(data)

# convert a string into a floating point number
print(float('0.9731'))

# calculate the mean value for a list of floating point numbers
values = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
print(statistics.mean(values))
