# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Georgia Brown
# Date given to class: 9/09/2022
# Date of Submission: 9/15/2022
# Description: Week 3 Lab - Compound Interest Lab
# Input: Users Initial principal balance, years in acct, times interest compounded per year and interest rate
# Output: Ending balance on account with interest added
# Additional Comments: Version 2

y = int(input('How many periods?'))
P = float(input('Please enter Initial principal amount: '))
r = float(input('Please enter Annual Interest rate amount: '))
n = int(input('Please enter Number of compounding periods per year: '))
t = int(input('Please enter Number of years you would like to save: '))
A = P * (pow((1 + r / n), n * t))

print("Your compound Interest Balance would be:", round(A, 2))