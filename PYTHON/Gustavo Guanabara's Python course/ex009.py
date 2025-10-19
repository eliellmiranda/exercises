# Write a program that reads any integer and displays its multiplication table.

print('-------------------------------------------')
print('=== WELCOME TO THE MULTIPLICATION TABLE ===')
print('-------------------------------------------')

number = int(input('Enter the number you want to see the multiplication table for: '))

counter = 1
for i in range(10):
   mult = number * counter
   print("{} x {} = {}".format(number, counter, mult))
   counter += 1