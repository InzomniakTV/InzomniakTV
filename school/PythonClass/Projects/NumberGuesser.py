# Number guesser v0.1

from random import *
x = (randint(1, 10))

print("Let's play a game!")

y = int(input("Pick a number 1-10: "))
if (y >= 1, y <= 10):
    print("So, you've chosen", int(y), 'it seems.')
else:
    y = int(input('Try again I said 1-10, moron...'))

if (y == x):
    print('Wow you guessed the right number it really was', int(x), 'holy crap!')
else:
    print('HAHA Idiot, it was', int(x), 'you dingleberry!  TRY AGAIN!')
