---
tag: 100daysofcoding, python, randomization, lists
---

# Notes
`Import random`: A module
`random.randint(a,b)`: Generate a random number between and including a and b 
Module: Function
`random_float = random.random()`: Random float generator between 0 and 1 but not including 1

Lists are contained in square brackets and the elements are separated by commas.
List index starts at zero. Think of as offset from beginning of list. 
Negative indexing is also possible, starts at the end of the list at -1
Using index you can modify elements in the list.
`list.append()`: Adding to the end of the list

IndexError: Tring to use an index out of the list size, usually by one due to offset
Nested List: List within a list
# Coding Exercises
## Exercise 1. Heads or Tails
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
### Sample Solution 1
``` python 
import random

coin_outcome = random.randint(0,1)

if coin_outcome == 0:
    print("Heads")
elif coin_outcome == 1:
    print("Tails")

```

## Exercise 2.  Banker Roulette
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Given:
``` python 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
```
### Sample Solution 2
``` python 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

payNum = random.randint(0,len(names)-1)
print(f"{names[payNum]} is going to buy the meal today!")
```

#### Using Choice Function
``` python 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

payNum = random.choice(names)
print(payNum + " is going to buy the meal today!")

```

## Exercise 3. Treasure Map
You are going to write a program that will mark a spot with an 'X'. 
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:
`[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]`
Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
The **first digit** in the input will specify the **column** (the position on the horizontal axis).
The **second digit** in the input will specify the **row** number (the position on the vertical axis).

Given: Remember that nested lists are accessed from out to in. So if `list=[[A,B,C],[E,F,G]]` then `E = list[1][0]`
```python
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

print(f"{row1}\n{row2}\n{row3}")
```
### Sample Solution 3
```python
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

input_row = int(position[0])
input_column = int(position[1])
map[input_column-1][input_row-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
```
## Day 4 Project: Rock Paper Scissors
Create a game of rock, paper, scissors where the player goes against the computer. The computer will produce a random choice each time.
Given:
rock = ASCII art
paper = ASCII art
scissors = ASCII art
### Sample Solution Day 4 
```python
import random

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computerChoice = random.randint(0,2)

RTS_Choices = [rock, paper, scissors]
if playerChoice > 2 or playerChoice < 0:
  print("Invalid input")
else:
  print(RTS_Choices[playerChoice])
  print("Computer chose:\n" + RTS_Choices[computerChoice])
  if playerChoice == computerChoice:
    print("You draw")
  elif playerChoice == 0 and computerChoice == 1:
    print("You lose")
  elif playerChoice == 0 and computerChoice == 2:
    print("You win")
  elif playerChoice == 1 and computerChoice == 0:
    print("You win")
  elif playerChoice == 1 and computerChoice == 2:
   print("You lose")
  elif playerChoice == 2 and computerChoice == 0:
    print("You lose")
  elif playerChoice == 2 and computerChoice == 1:
    print("You win")
```