# Create a program that reads how much money a person has and shows how many
# dollars they can buy. [Consider US$ 1.00 = R$ 5.00]

print('--------------------------------------')
print('=== WELCOME TO THE ONLINE EXCHANGE ===')
print('--------------------------------------')

real_amount = float(input('Enter the amount of money in R$ (Brazilian Real): '))

dollars = real_amount / 5

print(f'With R$ {real_amount:.2f}, you can buy US$ {dollars:.2f}')
