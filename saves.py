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

    flag = False
    tempRows = []

    for row in f1reader:
        if row[0].lower() == usrDel.lower():
            flag = True
        else:
            tempRows.append(row)
            
    if flag:
        f1.close()
        f1 = open('savedsheet.csv', 'w', newline='')
        f1writer = csv.writer(f1)
        f1writer.writerows(tempRows)
        f1.close()
        print('---Deleted successfully.')
    
    else:
        print('Error: City not found for deletion, hence not deleted.')
        
def serCity():
    f1 = open('savedsheet.csv', 'r', newline='')
    f1reader = csv.reader(f1)
    
    usrQuery = input('Enter city to search : ')
    
    for row in f1reader:
        if row[0].lower() == usrQuery.lower():
            print(row)
            break
    else:
        print('Error: City Data search unsuccessful.')

def editCity():
    f1 = open('savedsheet.csv', 'r', newline='')
    f1reader = csv.reader(f1)

    usrEdit = input('Enter city to edit data for: ')

    flag = False
    tempRows = []
    
    for row in f1reader:
        if row[0].lower() == usrEdit.lower():
            flag = True
            
        tempRows.append(row)

    if not flag:
        print('Error: City does not exist for editing, hence not edited.')
        return

    f1.close()

    if flag:
        while True:
            print('1. Change City name')
            print('2. Change Condition')
            print('3. Change Temperature')
            print('4. Change UV Index')
            print('5. Finish editing')
            #print('debug: ',tempRows) # DEBUG
            usrchoice = int(input('Enter Choice : '))

            if usrchoice == 1:
                ename = input('Enter name : ')
                for i in range(len(tempRows)):
                    if tempRows[i][0].lower() == usrEdit.lower():
                        tempRows[i][0] = ename
                print('--- Changed name.')

            elif usrchoice == 2:
                econd = input('Enter condition : ')
                for i in range(len(tempRows)):
                    if tempRows[i][0].lower() == usrEdit.lower():
                        tempRows[i][1] = econd
                print('--- Changed condition.')

            elif usrchoice == 3:
                etemp = input('Enter temperature : ')
                for i in range(len(tempRows)):
                    if tempRows[i][0].lower() == usrEdit.lower():
                        tempRows[i][2] = etemp
                print('--- Changed temperature.')

            elif usrchoice == 4:
                euv = input('Enter UV index : ')
                for i in range(len(tempRows)):
                    if tempRows[i][0].lower() == usrEdit.lower():
                        tempRows[i][3] = euv
                print('--- Changed UV index.')

            elif usrchoice == 5:
                break

            else:
                print('Error: Wrong choice.')

        # Write the edited rows back into the file
        f1 = open('savedsheet.csv', 'w', newline='')
        f1writer = csv.writer(f1)

        f1writer.writerows(tempRows)

        f1.close()



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
            
        elif usrChoice == 4:
            cls()
            
            serCity()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 5:
            cls()
            
            editCity()
            
            input('--Press ENTER to go back.')
            cls()
            
        elif usrChoice == 6:
            break
        
        else:
            input('Error: Wrong choice. Press ENTER to go back.')