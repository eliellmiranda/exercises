# Create a program that reads any real number and shows its integer part

import math
x = float(input('Enter a number: '))
print('The number entered was {} and its integer part is {}'.format(x, math.trunc(x)))

# Instead of importing, you could use the 'int' type in place of 'float'.
