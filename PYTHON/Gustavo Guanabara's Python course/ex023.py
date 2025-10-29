""" Write a program that reads a number from 0 to 9999 and 
displays each of its digits separately.
Example: 1834 → Unit: 4; Ten: 3; Hundred: 8; Thousand: 1 """

number = int(input('Enter a number: '))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print(f'The entered number was: {number}!')
print('UNIT: {}\nTEN: {}\nHUNDRED: {}\nTHOUSAND: {}'.format(unit, ten, hundred, thousand))

