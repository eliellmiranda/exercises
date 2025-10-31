""" Write a program that reads a car's speed.
If it exceeds 80 km/h, display a message saying the driver has been fined.
The fine costs $7.00 for each km above the limit. """

print('*** SPEED RADAR ***')
speed = float(input('Enter the vehicle speed: '))

if speed > 80:
    print('YOU HAVE BEEN FINED FOR SPEEDING\nThe fine amount is ${:.2f}'.format((speed - 80) * 7))
else:
    print('The speed is within the allowed limit.')
