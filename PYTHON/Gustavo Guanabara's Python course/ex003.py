#A simple script that prompts the user for two numbers, calculates their sum, and prints the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

print("The sum between {} and {} is: {}.".format(num1, num2, sum))