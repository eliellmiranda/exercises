# Write a program that reads a person's full name
# and then shows the first and last name separately

name = str(input('What is your name? ')).strip()
separated = name.split()
print('Your first name is: {}\nYour last name is: {}'.format(separated[0], separated[-1]))  # or .format(separated[0], separated[len(name) - 1])
