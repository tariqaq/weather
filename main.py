from utils import *

def main():
    
    while True:
        cls()
        
        print('---WEATHER FORECAST---')
        
        print('1. Show weather\n'
            '2. Saved Data\n'
            '3. Exit Program')
        
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            cls()
            print('weather.')
            input('Press ENTER to go back')
            cls()
        elif usrChoice == 2 :
            cls()
            print('saved datas.')
            input('Press ENTER to go back')
            cls()
        elif usrChoice == 3 :
            print('---Exiting Program---')
            break
    
    
main()