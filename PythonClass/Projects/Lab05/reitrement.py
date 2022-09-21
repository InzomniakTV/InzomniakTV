# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Georgia Brown
# Date given to class: 9/19/2022
# Date of Submission:
# Description: Week 5 Lab - Retirement
# Input: retirement pay
# Output: retirement contribution
# Additional Comments: Version 1

CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float("Enter any bonuses: ")
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross_pay)