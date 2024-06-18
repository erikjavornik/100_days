---
tag: 100daysofcoding, python, functions, output
---

# Notes
```python
def my_function()
	result = 3*2
	return result
output = my_function
```
Whatever is returned will replace the function call. output = 6

.title function: Capitalize the first letter of each word and lower case all other letters
ex.
``` python
def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

print(format_name("nAmE", "NaMe"))
```
Output: Name Name

Return word will cause exit of the function. For above example, a print statement after the return line will not be executed. Return can be empty

Docstring: First line after defining a function and in between three quotes 
(""" Information """)
# Coding Exercises
## Exercise 1. Days in Month
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.

You are then going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.

```plaintext
days_in_month(year=2022, month=2)
```

And it will use this information to work out the **number of days in the month**, then **return** that as the **output**, **e.g.:**

```plaintext
28
```

The List `month_days` contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
Given:
```python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")

def days_in_month():
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
   
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```
### Sample Solution 1
``` python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if input_month == 2:
    leap_year = is_leap(input_year)
    if leap_year == True:
        return 29
  return month_days[input_month-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)
```
## Day 10 Project: Calculator 
```python
#Calculator
from art import logo
#Add
def add(n1, n2):
  return n1 + n2
#Subtract
def sub(n1, n2):
  return n1 - n2
#Multiply
def mult(n1, n2):
  return n1 * n2
#Division
def div(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
```