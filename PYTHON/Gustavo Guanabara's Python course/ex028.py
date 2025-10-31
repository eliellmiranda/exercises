# Write a program that makes the computer "think" of a random integer
# between 0 and 5, and ask the user to try to guess which number
# was chosen by the computer. Then display whether the user won or lost.

import random, time
num = int(input('Enter a number between 0 and 5: '))

draw = random.randint(0, 5)
print('PROCESSING...')
time.sleep(2)

print('The chosen number was {}'.format(draw))

if num == draw:
    print("You got it right!")
else:
    print("You missed!")
