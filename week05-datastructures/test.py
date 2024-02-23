# randon.py
# a program that puts 10 random numbers in a list and prints one at a time
# Author: Paul O'Shaughnessy

import numpy as np
import random

queue = []
numberofnumbers = 10
rangeto = 100
for n in range(0, numberofnumbers):
    queue.append(random.randint(0, rangeto))
print(f'queue is {queue}')

while len(queue) != 0:
    currentnumber = queue.pop(0)
    print(f'current number is {currentnumber} and the queue is {queue}')

print('the queue is now empty')

