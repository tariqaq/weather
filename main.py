from utils import *
from weather import *
from saves import *

def main():
    
    while True:
        cls()
        
        print('---WEATHER FORECAST---'.center(globalCenter))
        
        print('1. Show weather\n'
            '2. Saved Data\n'
            '3. Exit Program')
        
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            cls()
            
            weatherMain()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 2 :
            cls()
            
            savesMain()
            
            input('---Press ENTER to go back.')
            cls()
            
        elif usrChoice == 3 :
            print('---Exiting Program---')
            break
        
        else:
            input('Error : Wrong choice. Press ENTER to go back.')
            
main()