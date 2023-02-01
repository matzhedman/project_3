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
* 

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