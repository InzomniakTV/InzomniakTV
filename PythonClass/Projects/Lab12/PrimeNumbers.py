# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: Don't Remember?
# Date of Submission: 10/30/2022
# Description: Make a star pattern thingy
# Input: Nothing from user.
# Output: uhh, an art project?
# Additional Comments:
# Version: 1.0

import math

num = int(input("Pick a number, any number!"))

def primer(n):
    if n == 2 or n == 3:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i == 0:
                return False
        return True

if primer(num) == True:
    print("Yay!  That's a prime number! :D")

else:
    print("Nope, not a prime number.  =[")
