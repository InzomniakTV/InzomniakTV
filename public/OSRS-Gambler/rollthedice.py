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

while cash >= 0:
    while bet >= cash:
        stake()

# I want this to do something where money auto sets it's denomination
# when it goes over/under certain thresholds and for it to show it's
# denomination whenever it prints the value "cash".  For now it's commented
# because if you run the script it fails, but this is a placeholder for a
# planned feature.  Will revisit later.
# def main(money):
