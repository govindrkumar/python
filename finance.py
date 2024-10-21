#!/usr/bin/env python
# coding: utf-8

import time

# Global Variables
finance = {}
amount_display = []  # Creating blank list

def display_menu():
    print("1. Add an expense\n2. View expense by Category\n3. View total expense\n4. Exit")
    return int(input("Choose option: "))  # Return the option chosen

def option_1():
    global finance, amount_display  # Declare as global to modify them
    category = input("Enter category: ")
    
    if category not in finance:
        finance[category] = {}  # Create blank dictionary for the category
    
    amount = float(input("Enter amount: "))  # Convert to float
    description = input("Enter description: ")
    
    finance[category]["amount"] = amount  # Add amount
    finance[category]["description"] = description  # Add description
    amount_display.append(amount)  # Add amount to the list

def display_detail():
    print("1. View category\n2. View Amount\n3. View full details\n\n")  # Fixed typo
    choose_choice = int(input("Select option: "))
    
    if choose_choice == 1:
        print(list(finance.keys()))  # Display categories
    elif choose_choice == 2:
        print(amount_display)  # Display amounts
    elif choose_choice == 3:
        print(finance)  # Display all details
    else:
        print("Invalid Option !!!!\n\n\n")
        display_detail()

def option_2():
    display_detail()  # Display details

def option_3():
    total_sum = sum(amount_display)  # Calculate total using built-in sum function
    time.sleep(3)
    print("Total expense is:", total_sum)

def main():
    while True:
        a = display_menu()  # Get user's choice
        if a == 1:
            option_1()  # Option 1 menu will appear
        elif a == 2:
            option_2()  # Option 2 menu will appear
        elif a == 3:
            option_3()  # Option 3 menu will appear
        elif a == 4:
            exit()  # Exit the program
        else:
            print("Please try again!")  # Error handling

# Start the program
main()  # Calling main function to start

