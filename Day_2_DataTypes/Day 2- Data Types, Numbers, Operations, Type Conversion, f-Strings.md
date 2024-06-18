---
tag: 100daysofcoding, python, data types, numbers, operations, type conversion, f-strings
---

# Notes
len() cannot be used for numbers

Subscripting/Indexing: Using Square brackets to choose the  exact part of the number/string. Starts at 0

If numbers are placed in quotes it will be treated as a string
ex. ‘123’+’345’ will print out 123345 vs 123+345 will print out 468

Integers: Whole numbers positive or negative
Can use _ in place of commas in code to easily read large numbers

Float: Floating Point number. A number with  a decimal

Boolean: Only have two values- True or False

`type()` function can be used to check what data type a variable or etc is

str: can be used to convert to data type to a string

int: can be used to convert to data type to an int

float: can be used to convert to data type to a float

Math operation:
`+` Addition
`-`  Subtraction
`*` Multiplication
`/` Division
`**` Exponent
Follows PEMDAS

, Round to that number of decimal point ( 8 / 3 , 2    Two decimal places)
// Floor division: Answer is round down

Other form for operation: variable += 1 is the same as variable = variable + 1

f-String: Type f in front of the string. {} for variables. Converting of variable is automatic
ex. `f ”words {integer_variable} more words {boolean}” # Will not cause an error
# Coding Exercises
## Exercise 1. Data Types
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8.
Given: 
```Python
two_digit_number = input("Type a two digit number: ")
```
### Sample Solution 1
``` Python
two_digit_number = input("Type a two digit number: ")

digit_one = int(two_digit_number[0])
digit_two = int(two_digit_number[1])
sum_two_digit_number = digit_one + digit_two
print(sum_two_digit_number)
```
## Exercise 2. BMI Calculator
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. Convert the result to a whole number.

Given: 
``` Python
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
```
### Sample Solution 2
``` Python
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
new_bmi = int(bmi)
print(new_bmi)
```

## Exercise 3. Life in Weeks
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. It will take your current age as the input and output a message with our time left in this format: You have x days, y weeks, and z months left.

Given: There are 365 days in a year, 52 weeks in a year and 12 months in a year.
```Python 
age = input("What is your current age? ")
```

### Sample Solution 3
```Python 
age = input("What is your current age? ")

int_age = int(age)

remain_days =  365 * (90 - int_age)
remain_weeks = 52 * (90 - int_age)
remain_months = 12 * (90 - int_age)

print(f'You have {remain_days} days, {remain_weeks} weeks, and {remain_months} months left.')
```

## Day 2 Project: Tip Calculator
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
### Sample Day 2 Solution
```python
print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")
tip_percent = input("What percentage tip  would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")
amount_owed_by_each = float(bill_total)/int(num_people) * (1 + int(tip_percent)/100)
amount_rounded = round(amount_owed_by_each, 2)
amount_rounded = "{:.2f}".format(amount_owed_by_each)
print(f"Each person should pay: ${amount_rounded}")
```