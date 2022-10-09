# Inzomniak and Injured Sock Present -
#########################################
####### OSRS Python Gambler v1.3 ########
#########################################
# Project Started 9/28/2022

from random import *
cash = 300000000
bet = 50000000

print("Alright numbnuts, listen up.")
print("You're gonna waste your life chasing GP.")
input("When you press enter, you start with 300m, and will 50/50 you until 0.")

# Simple 50/50 flipper.
def stake():
    fight = (randint(0, 1))
    if fight == 1:
        print("Now you have {:,} gp".format(cash + bet))
    else:
        print("Now you have {:,} gp".format(cash - bet))

while cash >= 50000000:
        stake()
    else
        print("Game over.  Max Monies - ")
