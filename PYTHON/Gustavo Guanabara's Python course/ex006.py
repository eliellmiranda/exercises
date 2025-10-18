print('WELCOME!\nThis program calculates the double, triple, and square root of a number.')

num = int(input('Enter a number: '))

double = num * 2
triple = num * 3
square_root = num ** (1 / 2)

print('The double of the given number is: {}\nThe triple is: {}\nAnd its square root is: {:.2f}'.format(double, triple, square_root))
