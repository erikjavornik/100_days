# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:21:35 2023

@author: Erik.Javornik
"""
#Import dictionary with information
import Coffee_Menu

#Declare machine resource levels
water_level = Coffee_Menu.resources['water']
milk_level = Coffee_Menu.resources['milk']
coffee_level = Coffee_Menu.resources['coffee']
total_money = 0
transaction_list = []


def brew_drink_water(water):
    """Calculate the water level after brewing"""
    new_water = water_level - water
    return new_water


def brew_drink_milk(milk):
    """Calculate the milk level after brewing"""
    new_milk = milk_level - milk
    return new_milk

    
def brew_drink_coffee(coffee):
    """Calculate the coffee level after brewing"""
    new_coffee = coffee_level - coffee
    return new_coffee
       
    
def check_resources(milk, water, coffee):
    """Determine if there is enough resources in the machine to brew and display which resource is low"""
    if milk > milk_level:
        print("Sorry there is not enough milk.")
        return False
    elif water > water_level:
        print("Sorry there is not enough water.")
        return False
    elif coffee > coffee_level:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def process_coins():
    """Total the money inserted"""
    print("Please insert the coins.")
    pennies = int(input("How many pennies?: "))
    nickels = int(input("How many nickels?: "))
    dimes = int(input("How many dimes?: "))
    quarters = int(input("How many quarters?: "))
    total_paid = round(0.01 * pennies + 0.05 * nickels + 0.1 * dimes + 0.25 * quarters, 2)
    return total_paid


def transaction_success(cost, amount_paid):
    """Determine if the user paid enough or not"""
    difference = amount_paid - cost
    return difference
       
#Start and continue While loop
should_loop = True

while should_loop:
    #Standardize drink inputs
    user_input = input("What would you like? (espresso/latte/cappuccino: ").lower()
    #Accepts three different drink inputs
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        #Espresso dictionary doesn't contain milk so manual set
        if user_input == 'espresso':
            milk_used = 0
        else:
            milk_used = Coffee_Menu.MENU[user_input]['ingredients']['milk']
        #Obtain required ingredients from dictionary
        water_used = Coffee_Menu.MENU[user_input]['ingredients']['water']
        coffee_used = Coffee_Menu.MENU[user_input]['ingredients']['coffee']
        drink_cost = Coffee_Menu.MENU[user_input]['cost']
        
        #Determine if the machine was enough material inside to brew drink
        can_brew = check_resources(milk_used, water_used, coffee_used)
        if can_brew == True:
            paid = process_coins()                      
            change = round(transaction_success(drink_cost, paid), 2)
            #Add drink cost to a list of costs
            transaction_list.append(paid - change)             
            #Positive or 0 change means user paid enough for drink
            if change >= 0:
                #Gives change and sets new resource levels
                print(f"Here is your change ${change}.")
                water_level = brew_drink_water(water_used)
                milk_level = brew_drink_milk(milk_used)
                coffee_level = brew_drink_coffee(coffee_used)
                print(f"Here is your {user_input}. Enjoy!")
            #Negative change: not enough money paid
            else:
                print("Sorry, that's not enough money. Money refunded")
    #Stop loop/Shut off machine            
    elif user_input == 'off':
        should_loop = False
    #Totals the money and displays resource levels    
    elif user_input == 'report':
        for i in transaction_list:
            total_money += i
        print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${total_money}")
    #Other user inputs and loop continues
    else:
        print("Invalid input. Try again")