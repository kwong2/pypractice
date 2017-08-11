# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = input("What number do you want the divisors for ")

for num in range (number, 101):
	if num % number == 0:
		return num 



