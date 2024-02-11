# convert.py
# a program to take a monetary amount in the form x.xx (may be negative) and return it in cents
# Author: Paul O'Shaughnessy

num = float(input('Enter an amount in euro and cents: '))
conv = int(abs(num * 100))
print('That amount in cents is {}'.format(conv))

