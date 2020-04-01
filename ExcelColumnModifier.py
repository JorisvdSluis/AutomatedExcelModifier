import csv
import numpy as np
from re import sub
# startValue = 10
# columnName = input('What is de header of the column you want to change? ')
# shouldModifyAllRows = input('Do you want to modify all rows? y/n?  ') 

# if shouldModifyAllRows == 'y':
#     start = 0
#     end = 10
# else:
#     start = input('What is the first row number you would like to modify? ')
#     end = input('What is the last row number you would like to modify? ')

# valueType = input('What is the type of values you want to modify? number or text? n/t? ')
# if valueType == 'n':  
#    modification = input('How would you like to modify? combine(c) subtract(s) multiply(m) or devide(d) ? ')
# else: 
#     modification = input('Would you like to append(a) or replace(r) the value ? ')

# value = input('What is the value you would like to use? ')

# if modification == 'c':
#     print(startValue + float(value))
# elif modification == 's':
#     print(startValue - float(value))
# elif modification == 'm':
#     print(startValue * float(value))
# elif modification == 'd':
#     print(startValue / float(value))
# elif modification == 'a':
#     print( str(startValue) + value)
# else: 
#     print(value)

with open('persons.csv', 'w', encoding='utf-8-sig') as csvfile2:
        dict_writer = csv.writer(csvfile2, lineterminator = '\n')
        with open(r'D:\Users\jjori\Documents\CeVeDe\csv2\test2.csv', 'r', encoding='utf-8-sig') as csv_file:
            priceString = 'Variant Price'
            comparePriceString = 'Variant Compare At Price'
            reader = csv.reader(csv_file)
        
            # dict_reader = csv.DictReader(csv_file)
            # fieldnames = dict_reader.fieldnames

            headers =  next(reader)
            print(headers)
            priceIndex = headers.index(priceString)
            compareIndex = headers.index(comparePriceString)
            dict_writer.writerow(headers)
            for row in reader:
                print(len(row))
                
                row[priceIndex] = round(float(sub(r'[^\d.]', '',row[priceIndex])) * 1.04, 2)
                row[compareIndex] = round(float(sub(r'[^\d.]', '',row[compareIndex])) * 1.04, 2)
                dict_writer.writerow(row)
