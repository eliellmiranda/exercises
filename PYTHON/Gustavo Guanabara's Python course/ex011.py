""" Create an algorithm that reads the price of a product
and shows its new price with a 5% discount """

print('---------------------------------------')
print('=== WELCOME TO * DISCOUNTED PRICE * ===')
print('---------------------------------------')

price = float(input('Enter the product price to get a 5% discount: '))
discounted_price = price * 0.95

print(f'The price with a 5% discount is: $ {discounted_price:.2f}')
