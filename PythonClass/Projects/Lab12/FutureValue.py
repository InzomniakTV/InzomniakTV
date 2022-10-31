# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: Don't Remember?
# Date of Submission: 10/31/2022
# Description: Future capital worth for your bank.
# Input: Your bank balance.
# Output: Bank balance, after interest applied, after time passes.
# Additional Comments:
# Version: 1.0

bank = float(input("Enter current bank balance:"))
interest = float(input("Enter interest rate in decimal percent:"))
time = float(input("Enter the amount of time that passes in months:"))

def money(bank, interest, time):
    return bank * (1 + interest)**time


print("{:.2f}".format(money(bank, interest, time)))
