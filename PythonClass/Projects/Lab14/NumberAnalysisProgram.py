# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Georgia Brown
# Date given to class: 11/18/2022
# Date of Submission: 11/27/2022
# Description: Week 14 Lab - Number Analysis Lab
# Input: series of number user wants to find: The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list
# Output: The users data displayed on std output
# Additional Comments: V 1.0

pickle = int(input("How many number do you want to compare? "))

numbers = []
total = 0
for i in range(pickle):
    number = int(input('Enter a number as a integer: '))
    numbers.append(number)
    total += number
print('The lowest number in the list is', min(numbers))
print('The highest number in the list is', max(numbers))
print('The total in the list is', total)
print('The average in the list is', total / pickle)