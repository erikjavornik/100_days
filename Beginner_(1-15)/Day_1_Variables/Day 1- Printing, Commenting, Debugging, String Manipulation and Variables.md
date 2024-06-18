---
tag: 100daysofcoding, python, printing, commenting, debugging, string manipulation, variables
---

# Notes
[repl.it - Online python editor](https://replit.com/)

[Or python tutor](https://pythontutor.com/visualize.html#mode=edit)

`print()` function: Outputs what is inside parenthesis. 
Text/Strings need single or double quotes. Typically use single.
If string contains single quotes, in this case use double quotes outside and inverse for double quotes in the string.

For syntax errors: Can copy error and paste into Google. Stackoverflow is a resource for troubleshooting errors

(backslash)n in the print() to print to a new line
ex. `print('Hello world!'(backslash)n'Hello world!')`

String concatenation: Use + to combine string statements
ex. `print('Hello' + ' ' + 'World')`

Spacing and Indentation is really important in python. Can cause error if extra space is used at beginning of code.

`input()` function: A prompt for the user to input data in the console

pound sign (#): Used to write comments about code. Or shortcut Crtl+/

`len()` function: Returns length/number of characters of a string

Variable: Something that can be changed and store data in a code
# Coding Exercises
## Exercise 1. Printing
Write a program with the following output:

Day 1 - Python Print Function
The function is declared like this:
`print('what to print')`

### Sample Solution 1
```python
print('Day 1 - Python Print Function')

print('The function is declared like this:')

print("print('what to print')")
```
## Exercise 2. Debugging Practice
Find and fix the errors in the following lines of code: 
```python
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign."")
	print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```
### Sample Solution 2
print("Day 1 - String Manipulation")        
Error: Missing start "

print('String Concatenation is done with the "+" sign.')    
Error: Cannot use " inside of ". Will change output

print('e.g. print("Hello " + "world")')
Error: Tab/indentation error

print("New lines can be created with a backslash and n.")
Error: Extra ( after print statement
## Exercise 3. Input Function
Write a program that prints the number of characters in a user's name.
Given: `len()` function calculates the length of a string

### Sample Solution 3
``` python
userName = input("What is your name? ")
print( len(userName) )
```
## Exercise 4. Variables
Write a program that switches the values stored in the variables a and b.
Given code:
``` python
a = input("a: ")
b = input("b: ")
# Codeing Space

# Coding Space
print("a: " + a)
print("b: " + b)
```
### Sample Solution 4
``` python 
a = input("a: ")
b = input("b: ")

c=a
a=b
b=c

print("a: " + a)
print("b: " + b)
```

## Day 1 Project: Band Name Generator
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.

### Sample Solution Day 1
``` python 
print("Welcome to the Band Name Generator.")
userCity = input("What's the name of the city you grew up in?\n")
userPet = input("What's your pet name?\n")
print('Your band name could be ' + userCity + " " + userPet)
```