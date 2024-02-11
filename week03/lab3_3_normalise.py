# normalise.py
# a program to read a string, strip leading or trailing characters and converts to lower case
# Author: Paul O'Shaughnessy

rawstring = input('Please enter a string: ')
normalisestring = rawstring.strip().lower()
length1 = len(rawstring)
length2 = len(normalisestring)
print(f'That string normalised is: {normalisestring}')
print(f'We reduced the input string from {length1} to {length2} characters')
   