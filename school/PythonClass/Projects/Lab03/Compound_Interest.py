# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 9-12-2022
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments: V 1.0

P = float(input('Please enter Initial principal amount:   '))
r = float(input('Please enter Annual Interest rate amount:   '))
n = int(input('Please enter Number of compounding periods per year:   '))
t = int(input('Please enter Number of years you would like to save:    '))
A = P * (pow((1 + r / n), n * t))

print("Your compound Interest Balance would be:", round(A, 2))