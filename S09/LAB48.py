import csv

with open('LAB48_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print(' |'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            print("EOF")
            break




