# average.py
# a program that keeps reading numbers until the user enters zero, and then averages the numbers
# Author: Paul O'Shaughnessy

nums = []

number = int(input('Please enter a number (zero to quit): '))
while number != 0:
    nums.append(number)
    number = int(input('Please enter a number (zero to quit): '))

for values in nums:
    print(values)

avg = float(sum(nums)) / len(nums)
print(f'average is {avg}')