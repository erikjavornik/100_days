from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
drinks = Menu()

should_loop = True

while should_loop:
    user_choice = input(f"What would you like? {drinks.get_items()}: ").lower()
        
    if user_choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif user_choice == "off":
        should_loop = False
    else:
        user_drink = drinks.find_drink(user_choice)        
        can_brew = coffeeMaker.is_resource_sufficient(user_drink)
        if can_brew:
          paid_enough = moneyMachine.make_payment(user_drink.cost)
          if paid_enough:
             coffeeMaker.make_coffee(user_drink) 
          
          
    