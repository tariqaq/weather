import csv
from utils import *

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
            
            f1 = open('savedsheet.csv', 'r', newline='')
            f1reader = csv.reader(f1)
            
            for row in f1reader:
                print(row)
            input('---Press ENTER to go back.')
            f1.close()