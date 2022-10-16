# Inzomniak Public Code
# Number Guessser v0.3

from random import *
x = (randint(1, 10))
print("Let's play a game!")
print('------------------')
y = int(input("Pick a number 1-10: "))

if 1 <= y <= 10:
    print("So, you've chosen", int(y), 'it seems.')
else:
    y = int(input('Try again I said 1-10, moron...'))
