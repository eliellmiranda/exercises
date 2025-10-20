""" Write a program that asks for the number of kilometers driven
by a rented car and the number of days it was rented.
Calculate the total price to pay, knowing that the car costs $60.00 per day
and $0.15 per kilometer driven. """

km = float(input('Enter the number of kilometers driven: '))
days = float(input('Enter the number of days rented: '))

total = (0.15 * km) + (60 * days)

print(f'The total amount to pay is: $ {total:.2f}')
