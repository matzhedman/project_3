import gspread
import colorama
import os
import datetime
from colorama import Fore
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project_3') 

"""
To run the program: python3 run.py
"""


def start():
    """
    First view, asks you to type in your name.
    Name should be logged and be added to the summary in the end - not working yet.
    """
    print('\nHello, welcome to laundry booking!\n')
    print('Please type in your name to book a time,\nor to see current bookings.\n')
    print('____________\n')
    print(Fore.GREEN + 'Enjoy your day!')
    print(Fore.WHITE + '____________\n')
    print('Enter your name: ')
    name = input()

def mainMenu():
    """
    Menu. 
    Shows the day and date of today.
    """
    os.system('clear')
    x = datetime.datetime.now()
    print('____________\n')
    print("Date and time of today:")
    print(x.strftime("%A"))
    print(x.strftime("%x"))
    print('____________\n')

    print('MAIN MENU \n')
    print('1) Book a Time')
    print('2) Show all current Bookings')
    print('00) Back to Start\n')
    while True:
        try:
            choice = int(input('Type in number to choose an option: \n'))
        except ValueError:
            print("Not a valid number")

        if choice == 1:
            choose_a_day()
            break
        elif choice == 2:
            show_my_booking()
            break
        elif choice == 00:
            log_out()
        else:
            print('Not a valid number, please choose 1), 2) or 00).')

start_up = start()
menu = mainMenu()