import csv
import numpy as np
from re import sub
startValue = 10
columnName = input('What is de header of the column you want to change? ')
shouldModifyAllRows = input('Do you want to modify all rows? y/n?  ') 

if shouldModifyAllRows == 'y':
    start = 0
    end = 10
else:
    start = input('What is the first row number you would like to modify? ')
    end = input('What is the last row number you would like to modify? ')

valueType = input('What is the type of values you want to modify? number or text? n/t? ')
if valueType == 'n':  
   modification = input('How would you like to modify? combine(c) subtract(s) multiply(m) or devide(d) ? ')
else: 
    modification = input('Would you like to append(a) or replace(r) the value ? ')

value = input('What is the value you would like to use? ')

if modification == 'c':
    print(startValue + float(value))
elif modification == 's':
    print(startValue - float(value))
elif modification == 'm':
    print(startValue * float(value))
elif modification == 'd':
    print(startValue / float(value))
elif modification == 'a':
    print( str(startValue) + value)
else: 
    print(value)


# with open(r'D:\Users\jjori\Documents\CeVeDe\csv2\test2.csv', 'r+') as csv_file:
#     priceString = 'Variant Price'
#     comparePriceString = 'Variant Compare At Price'
#     reader = csv.reader(csv_file)
#     writer = csv.writer(csv_file)
#     # dict_reader = csv.DictReader(csv_file)
#     # fieldnames = dict_reader.fieldnames
#     # dict_writer = csv.DictWriter(csv_file, fieldnames=[fieldnames])
#     headers =  next(reader)
#     priceIndex = headers.index(priceString)

#     for row in reader:
#        print(len(row[0]))
#        if len(row[0]) == 0:
#            break
#        price = row[priceIndex]   
#        print(price)
#        writer.writerow(row)
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