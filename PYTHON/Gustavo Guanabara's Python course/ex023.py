""" Write a program that reads a number from 0 to 9999 and 
displays each of its digits separately.
Example: 1834 → Unit: 4; Ten: 3; Hundred: 8; Thousand: 1 """

number = input("Enter a number from 0 to 9999: ")

length = len(number)

if length == 1:
    print(f'Unit: {number[0]}')
elif length == 2:
    print(f'Unit: {number[1]}\nTen: {number[0]}')
elif length == 3:
    print(f'Unit: {number[2]}\nTen: {number[1]}\nHundred: {number[0]}')
elif length == 4:
    print(f'Unit: {number[3]}\nTen: {number[2]}\nHundred: {number[1]}\nThousand: {number[0]}')
else:
    print('Please enter a number between 0 and 9999!')
