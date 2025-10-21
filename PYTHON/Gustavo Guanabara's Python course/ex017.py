""" Create a program that reads the length of the opposite side and the adjacent side 
of a right triangle, calculates and displays the length of the hypotenuse. """

co = float(input('Enter the length of the opposite side (cm): '))
ca = float(input('Enter the length of the adjacent side (cm): '))

from math import hypot

hypotenuse = hypot(co, ca)

print(round(hypotenuse, 2))
