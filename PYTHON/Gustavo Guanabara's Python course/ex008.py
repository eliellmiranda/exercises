# Write a program that reads a value in meters and displays it converted into centimeters and millimeters.

print('-----------------------------------------')
print('=== WELCOME TO THE UNIT CONVERTER ===')
print('-----------------------------------------')

value_m = int(input('Enter a value in meters (m)\nto get its equivalent\nin centimeters and millimeters: '))

value_cm = value_m * 100
value_mm = value_m * 1000

print('{} m in centimeters = {} cm\nand in millimeters = {} mm'.format(value_m, value_cm, value_mm))
