""" Create a program that reads an employee's salary and shows their new
salary with a 15% increase """

print('-------------------------------------------------')
print('=== WELCOME TO THE SALARY INCREASE CALCULATOR ===')
print('-------------------------------------------------')

salary = float(input('Enter the current salary: '))

new_salary = salary * 1.15

print(f'The new salary after a 15% increase is: $ {new_salary:.2f}')
