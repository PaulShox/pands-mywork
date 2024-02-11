# sub.py
# a program to read two numbers and delete one from the other
# Author: Paul O'Shaughnessy

f_num = int(input('Enter first number: '))
s_num = int(input('Enter second number: '))
ans = f_num - s_num
print('{} minus {} is {}'.format(f_num, s_num, ans))