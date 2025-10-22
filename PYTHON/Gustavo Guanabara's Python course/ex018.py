# Create a program that reads any angle
# and displays the sine, cosine, and tangent
# of that angle

from math import sin, cos, tan, radians
ang = float(input("Enter the desired angle: "))

rad = radians(ang)         

sine = round(sin(rad), 2)
cosine = round(cos(rad), 2)
tangent = round(tan(rad), 2)

print(f'The sine of the given angle is: {sine}\nThe cosine: {cosine}\n and the tangent: {tangent}')