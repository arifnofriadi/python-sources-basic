import csv

with open('car_price_dataset.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)