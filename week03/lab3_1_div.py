# div.py
# a program that reads in two numbers, divides the first by the second; give int and remainder
# Author: Paul O'Shaughnessy

f_num = int(input('Enter first number: '))
s_num = int(input('Enter second number: '))
ansint = int(f_num // s_num)
ansrem =  int(f_num % s_num)
print('{} divided by {} is {} with remainder {}'.format(f_num, s_num, ansint, ansrem))