import csv
from utils import *
from weather import *

def displaySaves():
    f1 = open('savedsheet.csv', 'r', newline='')
    f1reader = csv.reader(f1)
    
    for row in f1reader:
        print(row)
    f1.close()

def addSaves():
    f1 = open('savedsheet.csv', 'a+', newline='')
    f1writer = csv.writer(f1)
    
    weatherData = None
    usrCity = None
    rawSearchData = None
    
    usrCity = input('Enter the city : ')
    
    rawSearchData = searchCity(usrCity)
    searchedCity = formatSearch(rawSearchData)
    weatherData = getCityData(searchedCity)
    
    tmpRow = [searchedCity, weatherData['current']['condition']['text'], weatherData['current']['temp_c'], weatherData['current']['uv']] # [cityname, condition, tempcelsius, uvindex]
    
    f1writer.writerow(tmpRow)
    f1.close() # SAVES THE FILE
              
def savesMain():
    while True:
        cls()
        
        print('---Saved Weather Data---')
        
        print('1. Display all Saved Cities\n'
              '2. Add City\n'
              '3. Remove City\n'
              '4. Search City\n'
              '5. Edit Saved City\n'
              '6. Go Back')
        
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            cls()
            
            displaySaves()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 2:
            cls()
            
            addSaves()
            
            input('---Press ENTER to go back.')
            cls()