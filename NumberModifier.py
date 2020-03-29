import csv
import numpy as np
from re import sub
with open(r'D:\Users\jjori\Documents\CeVeDe\csv2\test2.csv', 'r+') as csv_file:
    priceString = 'Variant Price'
    comparePriceString = 'Variant Compare At Price'
    reader = csv.reader(csv_file)
    writer = csv.writer(csv_file)
    # dict_reader = csv.DictReader(csv_file)
    # fieldnames = dict_reader.fieldnames
    # dict_writer = csv.DictWriter(csv_file, fieldnames=[fieldnames])
    headers =  next(reader)
    priceIndex = headers.index(priceString)

    for row in reader:
       print(len(row[0]))
       if len(row[0]) == 0:
           break
       price = row[priceIndex]   
       print(price)
       writer.writerow(row)
    #    if not ''.join(row).strip():
            # price = row[priceIndex]
            # price = (float(price[4:-1]) * 1.04)
            # price = row[priceString]
            # comparePrice = row[comparePriceString]
            # print(price, comparePrice)
            # price = float(sub(r'[^\d.]', '',price[4:-1])) * 1.04
            # print(price, comparePrice)
            #row[priceString] = price
     
        
        # dict_writer.writerow(row)
    # print(PriceColumnIndex)
# print(ComparePriceColumnIndex)