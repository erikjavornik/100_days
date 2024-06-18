---
tag: 100daysofcoding, python, higher or lower game
---

# Sample Solution
```python
#Import modules
import art
import game_data
import random
from replit import clear

#Generates a random number depending on the size of game_data dictionary
def rand_num():
  return random.randint(0,len(game_data.data)-1)

#Function to compare the two choices and return the winner's letter
def compare(index_A, index_B):
  choice_A = game_data.data[index_A]['follower_count']
  choice_B = game_data.data[index_B]['follower_count']
  
  if choice_A > choice_B:
    return 'a'
  elif choice_A < choice_B:
    return 'b'

#Initalize values for the 1st round A choice only once, counter for #player's score, and while loop condition
index1 = rand_num()
final_score = 0
should_loop = True

#While loop to continue as long as player guesses correctly
while should_loop:
  #index2 changes each loop iteration
  index2 = rand_num()

  #Ensures index1 and index2 are not the same
  while index1 == index2:
    index2 = rand_num()

  #Inital art and display
  print(art.logo)
  print(f"Compare A: {game_data.data[index1]['name']}, a {game_data.data[index1]['description']}, from {game_data.data[index1]['country']}")
  #Debug code:#
  print(game_data.data[index1]['follower_count'])
  print(art.vs)
  print(f"Against B: {game_data.data[index2]['name']}, a {game_data.data[index2]['description']}, from {game_data.data[index2]['country']}")
  #Debug code:# 
  print(game_data.data[index2]['follower_count'])

  #Player inputs choice
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Calls compare function and assigns value 'A' or 'B' to winner variable
  winner = compare(index1, index2)

  #New choice A is current Choice B 
  index1 = index2
  clear()

  #Determine if player made the right choice. If correct, continue loop and increase score. If wrong, end loop and display score
  if winner == user_choice:
    final_score +=1
    print(f"Correct. Current score: {final_score}")
  else:
    print(art.logo)
    print(f"Incorrect. Final score: {final_score}")
    should_loop = False
```