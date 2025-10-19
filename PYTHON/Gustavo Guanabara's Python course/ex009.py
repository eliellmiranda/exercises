# Write a program that reads any integer and displays its multiplication table.

print('---------------------------')
print('=== WELCOME TO THE MULTIPLICATION TABLE ===')
print('---------------------------')

number = int(input('Enter the number you want to see the multiplication table for: '))

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")
