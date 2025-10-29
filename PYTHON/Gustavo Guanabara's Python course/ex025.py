# Create a program that reads a person's name
# and says whether it contains "silva" in it

name = str(input('Enter your full name: ')).strip()
print('Does your name contain Silva? {}'.format('silva' in name.lower()))
