import csv
from utils import *
from weather import *

def displaySaves():
    f1 = open('savedsheet.csv', 'r', newline='')
    f1reader = csv.reader(f1)
    
    for row in f1reader:
        print(row)
    f1.close()

def addCity():
    f1 = open('savedsheet.csv', 'a+', newline='')
    f1writer = csv.writer(f1)
    
    weatherData = None
    usrCity = None
    rawSearchData = None
    
    usrCity = input('Enter the city : ')
    
    rawSearchData = searchCity(usrCity)
    searchedCity = formatSearch(rawSearchData)
    weatherData = getCityData(searchedCity)
    
    f1 = open('savedsheet.csv', 'r', newline='') # CHECK if city already exists
    f1reader = csv.reader(f1)
    for row in f1reader:
        if row[0] == searchedCity:
            print('Error: City Data already exists, hence not added.')
            return
    
    tmpRow = [searchedCity, weatherData['current']['condition']['text'], weatherData['current']['temp_c'], weatherData['current']['uv']] # [cityname, condition, tempcelsius, uvindex]
    f1writer.writerow(tmpRow)
    print(f'---Added {searchedCity} weather data.')
    f1.close() # SAVES THE FILE

def delCity():
    f1 = open('savedsheet.csv', 'r', newline='')
    f1reader = csv.reader(f1)
    
    usrDel = input('Enter city to delete data for: ')
    
    tempRows = [] # nested list having all rows of original
    for row in f1reader:
        if row[0].lower() != usrDel.lower(): # adding all rows except for the one to be deleted
            tempRows.append(row)
    else:
        print('Error: City Data not found for deletion, hence not deleted.')
    f1.close()
    
    f1 = open('savedsheet.csv', 'w', newline='')
    f1writer = csv.writer(f1)
    f1writer.writerows(tempRows) # write all rows except for deleted one

def savesMain():
    while True:
        cls()
        
        print('---Saved Weather Data---')
        
        print('1. Display all Saved Cities data\n'
              '2. Add City data\n'
              '3. Delete City data\n'
              '4. Search City data\n'
              '5. Edit Saved City data\n'
              '6. Go Back')
        
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            cls()
            
            displaySaves()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 2:
            cls()
            
            addCity()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 3:
            cls()
            
            delCity()
            
            input('---Press ENTER to go back.')
            cls()
            
        