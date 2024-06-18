---
tag: 100daysofcoding, python, scope
---

# Notes:
Ex. Two apple trees. One is inside of a fence, the other is outside the fence. The one inside can only be accessed inside of the fence. The outside can be accessed by everyone

Local Scope: Exists within a function
Global Scope: Available anywhere in the code. Declared in main code

Important to track where a variable is declared. 
Ex:
```python
player_health = 10

def game():
	def drink_potion():
		potion_strength = 2
		print(player_health)
	#No error since within the four walls of the game() function
	drink_potion()

#Error. Not defined at this scope
drink_potion()
```
Python does not have block scope. A variable declared in an if statement block, it is still available in the rest of the code.
TLDR: If you create a variable within a function, then it's only available within that function. If you create a variable within an if block, while loop, etc., that does not count as creating a separate local scope.

Two separate variables can have the same name (Not recommended)
Ex.
```python 
enemies = "Skeleton"

def increase_enemies():
  enemies = "Zombie"
  print(f"enemies inside function: {enemies}")
	
increase_enemies()
print(f"enemies outside function: {enemies}")
```

Use global to modify a global scope in a local scope (Probably not used often). Prone to causing bugs and errors
``` python
enemies = 1

def increase_enemies():
  global enemies
  #Without the global enemies, there will be an error, since enemies has no initial value within the function
  enemies +=1
  print(f"enemies inside function: {enemies}")
	
increase_enemies()
print(f"enemies outside function: {enemies}")
```
Global Constants: Values that you never plan on changing (pi). Naming convention is to write in all CAPITALS
# Day 12 Project: The Number Guessing Game
```python
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

correct_guess = random.randint(1, 100)

#print(f"The answer is {correct_guess}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  num_guesses = 10
elif difficulty == 'hard':
  num_guesses = 5

should_loop = True

while should_loop:
  if num_guesses == 0:
    print(f"You ran out of guesses. The right number was {correct_guess}.")
    break
  
  print(f"You have {num_guesses} attempts remaining to guess the number.")
  user_guess = int(input("Guess a Number: "))
  
  
  if user_guess > correct_guess:
    print("Too high.")
    num_guesses -= 1
  elif user_guess < correct_guess:
    print("Too low.")
    num_guesses -= 1
  elif user_guess == correct_guess:
    print(f"Correct. The number was {correct_guess}")
    should_loop = False

  if num_guesses > 0 and should_loop == True:
    print("Guess again.")
  
```