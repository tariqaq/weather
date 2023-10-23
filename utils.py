import os

globalCenter = 45

def cls():
    if os.name == 'nt':  # nt based system
        os.system('cls')
    else:
        os.system('clear')  # unix based system