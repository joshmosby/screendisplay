import csv
import time

names = []
year = []

def current_date():
    day = int(time.strftime("%d"))
    month = (time.strftime("%b"))
    year = int(time.strftime("%y"))
    date = [day, month, year]
    return date
                         


def find_anniversary():
    with open('AnniversaryData.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ",")
        for row in readCSV:
            doh = row[2]
            if doh == 'DOH':
                continue
            doh = doh.split("-")
            
            
            try:
                doh[0] = int(doh[0])
                doh[2] = int(doh[2])
            except ValueError:
                if i == 'DOH':
                    break
            today = current_date()
            name = row[0]
            name = name.split(",")
            if doh[0] == today[0] and doh[1] == today[1]:
                return name[1],name[0]
                
            
            


    
