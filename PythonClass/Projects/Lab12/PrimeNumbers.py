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

def primer(n):
    if n == 2 or n == 3:#if n is 2 or 3 it's prime
        return True
    elif n%2 == 0:#if it's divisible by 2 otherwise, it isn't prime
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i == 0:
                return False
        return True

num = int(input("Pick a number, any number!"))
print(primer(num))
