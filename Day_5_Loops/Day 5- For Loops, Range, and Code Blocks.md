---
tag: 100daysofcoding, python, for loops, range, code blocks
---

# Notes
`for item in list_of items`: Loop will repeat for each item in list. Value of "item" will be assigned to item in list. Multiple lines of code can be looped, but must be indented correctly in the for loop. Lines after Loop will only execute after the loop is finished running. Good practice is to use the singular form of the word in the list. (Example bellow FRUIT in FRUITS).
ex.
```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
```
1st loop: fruit = "Apple"
2nd loop: fruit = "Peach"
3rd loop: fruit = "Pear"

Output:
Apple
Peach
Pear

`max()` : Gives the highest value in a list
`min()`: Gives the lowest value in a list

`for num in range(a, b)`:  For loop will repeat on the range specified. Last digit will not be included in the range. EX. range(1,10) will repeat from 1 to 9
range(1,11,3): number will increase by three; 1, 4, 7, 10

# Coding Exercises
## Exercise 1. Average Height
Write a a program that calculates the average student height from a List of heights, without the len() or sum( ) function.
Given:
```python
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
```
### Sample Solution 1
```python
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
sum_num = 0

for height in student_heights:
   sum_height += height

for num in student_heights:
    sum_num += 1

average_height = round(sum_height/sum_num)

print(average_height)
```
## Exercise 2. High Score
Write a program that calculates the highest score from a List of scores using for loops (no max() function)
Given:
```python
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)
```
### Sample Solution 2
```python
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
```
## Exercise 3. Adding Even Numbers
Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100.
### Sample Solution 3
```python
sum_even = 0

for number in range(2, 101, 2):
    sum_even += number

print(sum_even)
```
## Exercise 4. FizzBuzz
Write a program that automatically prints the solution to the FizzBuzz game.
> Your program should print each number from 1 to 100 in turn.
> When the number is divisible by 3 then instead of printing the number it should print "Fizz".
> When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
>   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
### Sample Solution 4
```python
for number in range(1, 101):
# Check Divisible by 3 and 5 first, other wise numbers like 15 will be given the wrong output
	#Check Divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    #Check Divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    #Check Divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # Print all other numbers    
    else:
        print(number)
```
## Day 5 Project: Password Generator 
The objective is to take the inputs from the user to these questions and then generate a random password.
Given:
```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
```
### Sample Solution Day 5 Project
```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
# Generate Random item from List letters
for letter in range(0, nr_letters + 1):
  password += random.choice(letters)
# Generate Random item from List symbols
for symbol in range(0, nr_symbols + 1):
  password += random.choice(symbols)
# Generate Random item from List numbers
for number in range(0, nr_numbers + 1):
  password += random.choice(numbers)

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for letter in range(0, nr_letters + 1):
  password_list.append(random.choice(letters))
for symbol in range(0, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for number in range(0, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"You password is: {password}")
```