import csv
import numpy as np
from re import sub

SerialNumbers = ['MINW', 'VERW', 'TEMW', 'STRW', 'COLO']

with open(r'C:\Users\jjori\Documents\CeVeDe\prijslijst 01-2023\jaga.csv', 'r', encoding='utf-8-sig') as origin:
      with open(r'C:\Users\jjori\Documents\CeVeDe\prijslijst 01-2023\jagaformat.csv', 'w', encoding='utf-8-sig') as result:
        resultDict_writer = csv.writer(result, lineterminator = '\n')
        orginReader = csv.reader(origin)
        try:
            for originRow in orginReader:
                if(len(originRow) > 2 and any(ele in originRow[0] for ele in SerialNumbers)):
                    
                    originRow[2] = originRow[2].strip().replace('€ ', '').replace('"', '').replace(',', '')
                    
                    #print(originRow[2])
                    resultDict_writer.writerow([originRow[0], originRow[2]])
                    
                        
        except:
            print('fail')