---
tag: 100daysofcoding, python, conditional statements, logical operators, code blocks, scope
---

# Notes
if else statement: Used to test condition and change the output depending on if condition is true or false. Indentation matters
Ex.
```Python
if height > 120:
	print("You can ride the rollercoaster!")
else:
	print("Sorry, you have to grow taller before you can ride.")
```

Comparison Operators: 
(>) Greater than
(<) Less than
(>=) Greater than or equal to
(<=) Less than or equal to
== Is equal to

% Modulo Gives the remainder

Nested if statements: Multiple condition need to checked
``` python 
if condition:
	if another condition:
		do this
	else:
		do this
else:
	do this

# elif: Use to test a second condition if needed

if condition:
	if condition A:
		do this
	elif condition B:
		do this
	else:
		do this
else:
do this
```
Logical Operators:
or, and, not

`variable.lower()`: All letters in variable are changed to lowercase
`variable.count(“a”)`: Count the number of time “a” (Not in including “A”) appears in variable
`\` can be used to ignore quotes in a string
# Coding Exercises
## Exercise 1. Odd or Even
Write a program that works out whether if a given number is an odd or even number.

Given: Even numbers can be divided by 2 with no remainder.
```Python 
number = int(input("Which number do you want to check? "))
```
### Sample Solution 1
```Python 
number = int(input("Which number do you want to check? "))

if number%2 == 0:
	print("This is an even number.")
else:
	print("This is an odd number.")
```


## Exercise 2. BMI 2.0
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
Round the result to the nearest whole number.
It should tell them the interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

Given: 
``` Python 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
```
### Sample Solution 2
``` Python 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
	print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clincically obese.")
```

## Exercise 3. Leap Year
Write a program that works out whether if a given year is a leap year.

This is how you work out whether if a particular year is a leap year.
On every year that is evenly divisible by 4 
Except every year that is evenly divisible by 100 
Unless the year is also evenly divisible by 400

Given: 
```Python
year = int(input("Which year do you want to check? "))
```

### Hint: Logic Diagram
![[Pasted image 20230612112746.png]]
#### Sample Solution 3
```Python
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year")
    else:
        print("Leap year.")
else:
  print("Not leap year.")
```

## Exercise 4. Pizza Order
Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill:
- Small Pizza: $15
- Medium Pizza: $20
- Large Pizza: $25
- Pepperoni for Small Pizza: +$2
- Pepperoni for Medium or Large Pizza: +$3
- Extra cheese for any size pizza: + $1

Given:
``` Python
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
```
### Sample Solution 4
``` Python
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is: ${bill}.")
```

## Exercise 5. Love Calculator
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
 Take both people's names and check for the number of times the letters in the word TRUE occurs. 
 Then check for the number of times the letters in the word LOVE occurs. 
 Then combine these numbers to make a 2 digit number.
 
For Love Scores **less than 10** _or_ **greater than 90**, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores **between 40** and **50**, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

Given: 
lower() function changes all the letters in a string to lowercase
count() function gives the number of times a letter occurs in a string
```Python
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
```

### Sample Solution 5
```Python
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combine = name1 + name2
name_combine_lower = name_combine.lower()

num_t = name_combine_lower.count("t")
num_r = name_combine_lower.count("r")
num_u = name_combine_lower.count("u")
num_e = name_combine_lower.count("e")
love_score_1 = num_t + num_r + num_u + num_e

num_l = name_combine_lower.count("l")
num_o = name_combine_lower.count("o")
num_v = name_combine_lower.count("v")
num_e = name_combine_lower.count("e")
love_score_2 = num_l + num_o + num_v + num_e

love_score = int(str(love_score_1)  + str(love_score_2))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
```

## Day 3 Project: Treasure Island
Make your own "Choose Your Own Adventure" game. Use conditionals such as `if`, `else`, and `elif` statements to lay out the logic and the story's path in your program. 
### Flow diagram:
![[Pasted image 20230612115833.png]]
### Sample Solution Day 3 Project
```Python 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

road = input("You start at a fork in the road. Do you take the left or right path? Type 'left' or 'right'. ").lower()

if road == "left":
  river = input("Along the path you come across a river. Do you swim across or wait for a boat? Type 'swim' or 'wait'. ").lower()
  if river == "wait":
    door = input("On the other side of the river, there are three metal doors. One blue, one red, andone yellow. Which door do you go through? Type 'blue', 'red', or 'yellow'. ").lower()
    if door == "yellow":
      print("Congradulations. You have found the treasure and are rich beyond your wildest dreams.")
    elif door == "red":
      print("You are incinerated in a fire. Game over")
    elif door == "blue":
      print("You are electrocuted when you place your hand on the door. Game over")
    else:
      print("Wrong or not an option. Heart attack. Game over")
  elif river == "swim":
    print("You are unable to do make it across and are attacked by a croc. Game over")
  else:
    print("Wrong or not an option. Heart attack. Game over")
elif road == "right":
  print("You fall in a trap hole lined with spikes. Game over")
else:
  print("Wrong or not an option. Heart attack. Game over")

```