# Laundry booking system

## Table of contents
* [Introduction](#Introduction)
    * [Site Goals](#Site-Goals)
    * [Target Audience](#Target-Audience)
    * [User stories](#User-Stories)
    * [Features Planned](#Features-Planned)
* [Structure](#Structure)
    * [Features](#Features)
    * [Features left to Implement](#Features-Left-to-Implement)
* [Logical Flow](#Logical-Flow)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Functional Testing](#Functional-Testing)
    * [Pep8 Validation](#Pep8-Validation)
    * [Bugs and Fixes](#Bugs-and-Fixes)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
* [Credits](#Credits)
  * [Content](#Content



## Introduction
This is a laundry booking system for small rental properties.

### Site Goals
* The purpose of the system is to simplify the actual booking procedure.
* To keep track of whom and which time Person X can do his/hers laundry. 

### Target Audience
* The audience of this booking system are tenants in rental properties. 

### User Stories
* As a user, I would like to be able to book a time for laundry that suits me.
* As a user, I would like to get an overview of which days and times the laundry room is free and not booked.
* As a user, I want to check my schedule bookings in an easy way.


### Existing Features
#### Start menu
* First when the program runs the user is being greeted and prompted to enter a name.
![start](/documents/images/pp3_start.png)

* After entering a name, the user will continue to a part where the todays date is displayed (updates for every day so it always will show current date).
* There is also three (3) options for the user to choose between:
![mainmenu](/documents/images/pp3_main_menu.png)

##### OPTION 1 ("1")
* Option "1) Book a Time" takes the user to the book menu and will first show a list of days, monday - sunday. Data comes from the spreadsheet.
![option1](/documents/images/pp3_option_1.png)
* After choosing a day, either one, by typing in a number between 1 to 7 and hit Enter, the program will continue to ask the user to choose a Time for laundry on that specific day. The user has four (4) options, see picture below:
![time](/documents/images/pp3_time.png)
* Coming this far the user has reached the last part of this section (Section: "1) Book a Time"). The user is asked to confirm the booking by typing "yes" or "no". "Yes" will take the user back to the start view. "No" will take the user back to choosing day for laundry.
![yes_no](/documents/images/pp3_yes_no.png)

##### OPTION 2 ("2")
* Option "2) Show all current Bookings" takes the user in to the view where the current booking for the chosen username is displayed. ALERT! This function is currently not working due to a bug in the system. Our developers are working on solving the problem. As for now, following messages is to be displayed when the function is working correctly:
    * Current booking exists
![show_booking](/documents/images/pp3_show_booking.png)
    * No current booking
![show_booking2](/documents/images/pp3_show_booking2.png)

##### OPTION 3 ("00")
* If neither option 1 or 2 is what the user wants, it's possible to log out of the laundry booking system by typing "00" and hit Enter. A short message in red in the top will appear, and next user is able to log in.
![log_out](/documents/images/pp3_log_out.png)    

## Structure
### Logical Flow
* I have created a flowchart of the structure for this program. Following flow is as the program works right now. See section of [Features left to Implement](#Features-Left-to-Implement) for the expected final version.
![flowchart_current](/documents/images/pp3_flowchart2.png)


### Features Left to Implement
* This is a flowchart of the expected final version. 
![flowchart_expected](/documents/images/pp3_flowchart.png)
* Features to implement:
    * Login-function that validates input data.
    * A function that requests data from spreadsheet with calender-data.
    * A Calender that shows the whole month, and all available days (not times in this stage to avoid too much information).
    * The possibility to choose an available time and after booking it, it should not appear as an available time for next user.
    * A function that requests data for current users booking, if any, from calender data in spreadsheet. Otherwise print a message of "{Username} has no current booking".
    * Validation of all input.

### Database design
* A worksheet using "Google Sheets" has been implemented as database in this program. Current version is only using the spreadsheet of "laundry_days" to display days (monday to sunday). See picture below.
![worksheet](/documents/images/pp3_worksheet.png)

## Technologies
* Python - Python was the main language to build this program.
    * Python packages used:
        - Colorama - this was used to add color to text.
    
    * Python module used:
        - gspread - this API was used to connect to Google Sheet API.
        - os - this module was used to import clear function of the terminal.
        - datetime - this module was used to show current date in the Main menu.
* Google Drive API - this was used to set upp credentials.
* Google Sheet - this was used as a database.

## Testing
### Functional Testing
    ----EMPTY---- 
    ----EMPTY---- 
    ----EMPTY---- 
    ----EMPTY----   



### Pep8 Validation
* Python syntax checker at [Extends class](https://extendsclass.com/python-tester.html) was used to check the code. No error was found.
![python-validator](/documents/images/pp3_python_validator.png)

### Bugs and Fixes
* start()
    * Name input validation not working, tried this in different variations:
	![name_validation](/documents/images/pp3_input_validation.png)

* mainMenu()
    * Validation doesn’t work. System crashes when anything else then 1, 2 or 00 is printed.
        * Fixed! credits below.

* choose_a_day()
    * Validation doesn’t work. System crashes when anything else then 1 to 7 is printed.
        * Partially fixed! See test result in [Functional Testing](#Functional-Testing).

* times()
    * Validation doesn’t work. System crashes when anything else then 1 to 4 is printed.
        * Partially fixed! See test result in [Functional Testing](#Functional-Testing).


* summary()
When typing anything else then ”yes” or ”no”; message not printed. Repeats the question.
	else:
        print('Please answer "yes" or "no". Try again!')
    summary()

* show_my_booking()
Can’t get this function to work. 




## Deployment

### Version Control

### Heroku Deployment

## Credits
### Code
* I used Code Institutes walkthrough project as tutorial for setting everything up and get the connection to my Worksheet, and also for steps to deploy my program to Heroku.

* [Clear function](https://www.scaler.com/topics/how-to-clear-screen-in-python/) - this tutorial was used to implement the [os.system('clear')] function and by looking at a project made by "Supersheep50". See credit below.
* [Change color on text](https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python) - this tutorial was used to implement color on text. 
    * [Fix the colorama error](https://blog.finxter.com/fixed-modulenotfounderror-no-module-named-colorama/) - this tutorial was used to understand and to install "pip install colorama"-package.
* [Datetime](https://www.w3schools.com/python/python_datetime.asp) - this tutorial was used to add datetime to Main Menu.
* For solving my navigation through the menus and getting the "clear"-function mentioned above; without him noticing a special thanks to "Supersheep50" and his project The-Secret-of-the-HLL-Tomb. 
