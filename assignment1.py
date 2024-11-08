#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: "Ranmunige Senitha Ransen Rajapaksha"
The python code in this file (a1_rsrrajapaksha.py) is original work written by
"Ranmunige Senitha Ransen Rajapaksha". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int: 
    '''return the maximum number of days for each month, also accounting for leap years.'''
    if month == 2:  # February - basically checks if the month is february
        if leap_year(year): #if the month is february and its a leap year
            return 29 # then we return the maximum day for the month is 29
        else: #otherwise if it is not a leap year
            return 28 # then we return the month max date as 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November - basically if the month is april, june, september or november
        return 30 # we return 30 as April, June, September, November has 30 days in total
    else:  # All other months - this accounts for all the other months such as January, March, May, July, August, October, December
        return 31 # we return 31 as the above months has 31 days in total

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-') # This splits the date that is input into year, month, and day, this helps us to work with the year, month and date seperately.
    year = int(str_year) #converts the string year into integer
    month = int(str_month) #converts the string month into integer
    day = int(str_day) #converts the string day into integer
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year): # This checks if tmp_day exceeds the maximum number of days in the current month using the mon_max function.
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 so that we can start from the next months 1st date 
        tmp_month = month + 1 #tmp_month is increased by 1 so that it moves to the next month
    else:
        to_day = tmp_day #if tmp_day doesn't does not exceed the months maximum then the to_day is set to tmp_day 
        tmp_month = month + 0 #and it also keeps the month unchanged as the date doesn't exeed the maximum number of days

    if tmp_month > 12: #here it checks if the tmp_month is greated than 12
        to_month = 1 # if the month is greater than 12 then it is reseted to 1 january basically
        year = year + 1 #and adds +1 to the year as this indicates that we are moving to the next year
    else:
        to_month = tmp_month + 0 #Here this is here if the next month is within the same year so no change to the year is made it just sets to_month as the tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}" #this constructs the next date in year, month and day format with 2 character padding for month and day

    return next_date #this returns the constructed string (this is the final output)


def usage():
    '''Print a usage message to the user'''
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    print("Ensure that both dates are in YYYY-MM-DD format.")


def leap_year(year: int) -> bool:
    ''' A leap year is divisible by 4, but not by 100 unless it is also divisible by 400 (When accounting for a century)'''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) # This code defines what a leap year is 

def valid_date(date: str) -> bool:
    '''check validity of date and return True if valid'''
    try:
        # Split the date into year, month, and day 
        str_year, str_month, str_day = date.split('-')

        # This helps us check if the date has the correct format: "YYYY-MM-DD"
        if len(date) != 10 or date[4] != '-' or date[7] != '-':
            return False
        
        # This helps us ensure that all parts are digits
        if not (str_year.isdigit() and str_month.isdigit() and str_day.isdigit()):
            return False

        year = int(str_year) #converts the strings into integer values
        month = int(str_month) #converts the strings into integer values
        day = int(str_day) #converts the strings into integer values

        # Check if the month is between 1 and 12
        if month < 1 or month > 12:
            return False

        # Check if the day is valid for the given month using mon_max
        if day < 1 or day > mon_max(month, year):
            return False

        # If no issues, return True as date is valid
        return True
    except (ValueError, IndexError):
        # Return False if there is any error 
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    weekend_count = 0
    current_date = start_date

    # This lets us Ensure that the start date is earlier or equal to the stop date
    if start_date > stop_date: # if start date is greater than stop date
        start_date, stop_date = stop_date, start_date #this swaps the values of start date and stop date, basically if the user inputs the dates in the wrong order, this helps to ensure that the start date is always earlier than the stop date

    # Loop through all dates from start_date to stop_date (inclusive)
    while current_date <= stop_date: 
        # Split the current date into year, month, and day
        year, month, day = map(int, current_date.split('-'))
        
        # Get the day of the week (e.g., 'sat', 'sun', etc.)
        day_name = day_of_week(year, month, day)

        # Increment count if it's a Saturday or Sunday
        if day_name in ['sat', 'sun']: #This is where saturdays and sundays are calculated, so if the day name comes to saturday or sunday weekend count is added by 1
            weekend_count += 1

        # Move to the next day using the after function
        current_date = after(current_date)

    return weekend_count

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        usage() # if the required number of arguments(3 arguments (The script name, start date, and stop date)) is not printed this prints the usage function instruction the user to use the correct format
        sys.exit(1) # This exits the program with status code 1 indicating an error as the required arguments has not been provided.

    # This enables us to get the start and stop dates from command-line arguments
    start_date = sys.argv[1] 
    stop_date = sys.argv[2]

    # This helps us Validate both dates using the valid date function
    if not valid_date(start_date) or not valid_date(stop_date):
        usage()
        sys.exit(1)

    # This helps us Calculate the number of weekend days
    weekend_days = day_count(start_date, stop_date) 

    # This prints the final output of the program
    print(f"The period between {start_date} and {stop_date} includes {weekend_days} weekend days.")
