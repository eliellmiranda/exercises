# Write a program that converts a temperature
# from ºC (Celsius) to ºF (Fahrenheit)
# F = C x 1.8 + 32

tempC = float(input('Enter the temperature in ºC (degrees Celsius): '))

tempF = (tempC * 1.8) + 32

print(f'The temperature {tempC:.1f}ºC is equivalent to:\n{tempF:.1f}ºF')
