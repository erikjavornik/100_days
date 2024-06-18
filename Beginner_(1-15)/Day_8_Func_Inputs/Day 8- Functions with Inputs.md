---
tag: 100daysofcoding, python, functions, input
---

# Notes
`def function(Something)`
>	`Do this with Something`

Parameter: The variable or name of the data defined in the function
Argument: The value or piece of data being passed to the function

Functions with multiple inputs: 
`def function(something, somewhere)`

Positional Argument: When the function is called, the arguments are assigned to the parameters by the position

`def function(a, b, c)`
>`Do this with a`
>`Then this with b`
>`And this with c`

Call above function:
`function(1, 2, 3)`
For this call: a = 1, b = 2,  c =3
`function(3, 1, 2)`
For this call: a = 3, b = 1, c =2

Keyword Arguments:
`function(a = 1, b = 2,  c =3)`
For this call: a = 1, b = 2,  c =3
`function(c = 3, a = 1, b = 2)`
For this call: a = 1, b = 2,  c =3

Round up a number:
`import math`
`math.ceil()`
# Coding Exercises
## Exercise 1. Paint Area Calculator
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
Given: number of cans = (wall height x wall width) ÷ coverage per can. Solution must be rounded up (Cannot buy half a can of paint)
``` python
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
```
### Sample Solution 1
``` python

import math

def paint_calc(height, width, cover):
    num_can = height * width / cover
    print(f"You'll need {math.ceil(num_can)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

```
## Exercise 2. Prime Numbers
You need to write a function that checks whether if the number passed into it is a prime number or not.
Given: 

``` python

n = int(input("Check this number: "))

prime_checker(number=n)

```
### Sample Solution 2
``` python

def prime_checker(number):
    num_check = False
    divide_num = number - 1

    while num_check == False:    
        if number == 1:
            print("It's not a prime number.")
            break
        div_answer = number % divide_num
        if divide_num == 1:
            print("It's a prime number.")
            num_check = True  
        elif div_answer == 0:
            print("It's not a prime number.")
            num_check = True
        else:
            divide_num -=1**

n = int(input("Check this number: "))
prime_checker(number=n)
```

## Cipher Project Step 1. Encode Function
```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
	position = alphabet.index(letter)
	new_position = position + shift_amount
	new_letter = alphabet[new_position]
	cipher_text += new_letter

print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text= text, shift_amount= shift)
```

## Cipher Project Step 2. Decode Function
``` python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
	position = alphabet.index(letter)
	new_position = position + shift_amount
	cipher_text += alphabet[new_position]

  print(f"The encoded text is {cipher_text}")
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(plain_text, shift_amount):
  decode_text = ""
  for letter in plain_text:
	position = alphabet.index(letter)
	new_position = position - shift_amount
	decode_text += alphabet[new_position]
  print(f"The decoded text is {decode_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(plain_text=text, shift_amount=shift)
else:
  print("Invalid directions.")
```

## Cipher Project Step 3. Combining Functions
``` python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(cipher_direction, start_text, shift_amount):
  output_message = ""
  for letter in start_text:
	position = alphabet.index(letter)
	if cipher_direction == "encode":
	  new_position = position + shift_amount
	elif cipher_direction == "decode":
	   new_position = position - shift_amount
	output_message += alphabet[new_position]

  print(f"The new text is {output_message}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(cipher_direction = direction, start_text = text, shift_amount = shift)
```
## Cipher Project Step 4.  Clean-up, Debugging, Beautify
``` python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
	shift_amount *= -1

 for char in start_text:
	if char in alphabet:
	   position = alphabet.index(char)
	   new_position = position + shift_amount
	   end_text += alphabet[new_position]
	else:
	   end_text += char

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

import art
print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

user_choice = True
while user_choice == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?

#Try running the program and entering a shift number of 45.

#Add some code so that the program continues to work even if the user enters a shift number greater than 26.

#Hint: Think about how you can use the modulus (%).

  if shift > 26:

	shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' to continue. Type 'no' to exit.\n")
  if result == 'no':
   user_choice = False
   print("Goodbye")**
```