import csv
import time

names = []
year = []

def current_date():
    day = int(time.strftime("%d"))
    month = int(time.strftime("%m"))
    year = int(time.strftime("%Y"))
    date = [day, month, year]
    return date
                         


def find_anniversary():
    with open('AnniversaryData.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ",")
        for row in readCSV:
            doh = row[2]
            doh = doh.split("-")
            for i in doh:
                try:
                    i = int(i)
                except ValueError:
                    if i == 'DOH':
                        break
                print (i)
                
            
            '''print (doh)'''

def returnppl():
    
