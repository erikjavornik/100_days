---
tag: 100daysofcoding, python, debugging
---

# Notes 

Find and fix the bug:
```python
############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
```
Solution
```python
############DEBUGGING#####################

# # Describe Problem
def my_function():
#20 is not included in the range function
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#Replace the randint with each number to test each value
#List index doesn't go up to 6 and will cause an error
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
## Run through the code as if you were the computer
#Input of 1994 will not trigger either statement
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
#Input is stored as a str and must be converted to an int for comparision
age = int(input("How old are you?"))
if age > 18:
	#Indentation error and not an f-string
	print(f"You can drive at age {age}.")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#== doesn't assign a value
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
##Use print statements to find 
# print(f"pages = {pages}")
# print(f"words = {word_per_page}")
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    #Use a debugger (Pyton tutor) to find were the problem occurs
    #Line needs to be a part of the for loop
	b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
```