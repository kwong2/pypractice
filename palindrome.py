# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
wrd = input("So what word should we check if it is a palindrome?")
wrd_reverse = wrd[::-1]

if wrd == wrd_reverse:
	print ("This word is a palindrome.")
else:
	print ("NOT!")