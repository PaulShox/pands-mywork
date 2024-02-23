# topthree.py
# a program that generates 10 random numbers and prints out the top three
# Author: Paul O'Shaughnessy

import random

numbers = random.sample(range(0, 101), 10)
print('10 random numbers: ', numbers)
numbers.sort(reverse=True)
tpthree = numbers[:3]
print('The top three are: ', tpthree)