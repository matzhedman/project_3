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

##### OPTION 1
* Option "1) Book a Time" takes the user to the book menu and will first show a list of days, monday - sunday. Data comes from the spreadsheet.
![option1](/documents/images/pp3_option_1.png)
* After choosing a day, either one, by typing in a number between 1 to 7 and hit Enter, the program will continue to ask the user to choose a Time for laundry on that specific day. The user has four (4) options, see picture below:
![time](/documents/images/pp3_time.png)
* Coming this far the user has reached the last part of this section (Section: "1) Book a Time"). The user is asked to confirm the booking by typing "yes" or "no". "Yes" will take the user back to the start view. "No" will take the user back to choosing day for laundry.


       
    

## Structure

### Features

### Features Left to Implement

## Logical Flow

## Technologies

## Testing

### Functional Testing

### Pep8 Validation

### Bugs and Fixes
#### Bugs
* start()
    * Name input validation not working, tried this in different variations:
	![name_validation](/documents/images/pp3_input_validation.png)
    

* mainMenu()
Validation doesn’t work. System crashes when anything else then 1, 2 or 00 is printed.

* choose_a_day()
Validation doesn’t work. System crashes when anything else then 1 to 7 is printed.

* times()
Validation doesn’t work. System crashes when anything else then 1 to 4 is printed.

* summary()
When typing anything else then ”yes” or ”no”; message not printed. Repeats the question.
	else:
        print('Please answer "yes" or "no". Try again!')
    summary()

* show_my_booking()
Can’t get this function to work, not even to print message. 


## Deployment

### Version Control

### Heroku Deployment

## Credits
### Code