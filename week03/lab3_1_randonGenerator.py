# randomGenerator.py
# first program prints out a random number between 1 and 10
# second program requires user input to select the range and print random number
# Author: Paul O'Shaughnessy

import random 

# number = random.randint(1, 10)
# print('here is a random number: {}'.format(number))

num1 = int(input('Enter first number in range: '))
num2 = int(input('Enter second number in range: '))
number = random.randint(num1, num2)
print('here is a random number between {} and {}: {}'.format(num1, num2, number))