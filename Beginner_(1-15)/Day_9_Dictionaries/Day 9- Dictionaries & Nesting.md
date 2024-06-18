---
tag: 100daysofcoding, python, nesting, dictionaries
---

# Notes
Dictionaries: Two parts, the key and value. Key is the word and value is the definition 
``{Key: Value}`` 
Good practice for dictionaries with multiple entries:
``` python
programming_dictionary
{
	"Bug": "An error in a program that prevents the program from running as expected.", 
	"Function": "A piece of code that you can easily call over and over again."
}
```
Common error is misspelling the key. And for strings, must be in "" when defined in the dictionary. Otherwise error will occur and python thinks it is an undefined variable

Can append a dictionary:
``` python
programming_dictionary["Loop"] = "The action of doing something over and over again."
```
Can declare an empty dictionary:
``` python
empty_dictionary = {}
```
Clearing out a dictionary:
Set dictionary to an empty dictionary
``` Python
programming_dictionary = {}
```
Editing a dictionary:
Set key in dictionary equal to something else
```python
programming_dictionary["Bug"] = "A moth in your computer"
```
Loop through a dictionary
```Python
for thing in programming_dictionary:
  print(thing)
```
This will output only the keys: Bug Function Loop
```Python
for thing in programming_dictionary:
  print(thing)
  print(programing_dictionary[thing])
```
Will output both key and value

To save multiple values to one key, use a list.
```python
travel_log = {
	"France": ["Paris", "Lille", "Dijon"],
	"Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
```

Nested Dictionary in a Dictionary
``` python
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], total_visits": 5},
}
```

Nesting Dictionary in a List
```python
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
```

# Coding Exercises
## Exercise 1. Grading Program
You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**.

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. T**he final version** of the `student_grades` dictionary will be checked.
This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"
> 
> Scores 81 - 90: Grade = "Exceeds Expectations"
> 
> Scores 71 - 80: Grade = "Acceptable"
> 
> Scores 70 or lower: Grade = "Fail"

Given:
```python
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

print(student_grades)
```
### Sample Solution 1
```Python
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding" 
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student]  <= 70:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇

print(student_grades)
```
## Exercise 2. Dictionary in Lists
You are going to write a program that adds to a `travel_log`. You can see a travel_log which is a **List** that contains 2 **Dictionaries**.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the `travel_log`.

```plaintext
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
```

> You've visited Russia 2 times.
> You've been to Moscow and Saint Petersburg.

Given:
``` python
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
```

### Sample Solution 2
``` python
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
```
## Day 9 Project: Silent Auction:
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually. 
### Sample Solution Day 9 Project
``` python
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the silent auction!")

stop_loop = False
all_bids = {}

while stop_loop == False:
  user_name = input("What is your name: ")
  user_bid = int(input("What is you bid: $"))
  other_bidders = input("Are there other bidders, type 'Y' or 'N': ")

  all_bids[user_name] = user_bid
  
  if other_bidders == 'Y':
    clear()
  elif other_bidders == 'N':
    stop_loop = True

highest_bid = 0

for bid in all_bids:
  if all_bids[bid] > highest_bid:
    highest_bid = all_bids[bid]
    highest_name = bid
print(f"The winner is {highest_name} with a bid of ${highest_bid}.")
```