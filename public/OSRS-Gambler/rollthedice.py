# Inzomniak and Injured Sock Present -
#########################################
####### OSRS Python Gambler v1.0 ########
#########################################

# Project Started 9/28/2022

from random import *
cash = 300000000

print("Alright numbnuts, listen up.")
print("You're gonna waste your life chasing GP.")
bet = int(input("Enter your first bet, it's a 50/50 chance: "))

# Simple 50/50 flipper.
def stake():
    fight = (randint(0, 1))
    if fight == 1:
        print("{:,}".format(cash + bet))
    else:
        print("{:,}".format(cash - bet))

stake()

# I want this to do something where money auto sets it's denomination
# when it goes over/under certain thresholds and for it to show it's
# denomination whenever it prints the value "cash".  For now it's commented
# because if you run the script it fails, but this is a placeholder for a
# planned feature.  Will revisit later.
# def main(money):
