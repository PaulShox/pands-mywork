# floor.py
# a program that takes in a float and outputs an int rounded down
# Author: Paul O'Shaughnessy

import math

num_to_floor = float(input('Enter a float number: '))
floored_num = math.floor(num_to_floor)
print('{} floored is {}'.format(num_to_floor, floored_num))