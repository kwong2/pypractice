# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Exercise 1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("What is your name?")
print ("Hello " + str(name))

age = input("How old are you?")
age = int(age)

print ("Your name is " + str(name) + " and you are " + str(age) + " years old")
years = int(100 - age)

print ("You will turn 100 in " + str(years) + " years.")

future = (2016 + years)
print (str(years) + " years from now is " + str(future))