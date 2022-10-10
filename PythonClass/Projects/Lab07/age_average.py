# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 10/10/2022
# Date of Submission: 10/10/2022
# Description: Average out ages.
# Input: 3 persons' age.
# Output: Average age of the 3 people.
# Additional Comments: V 1.0

me = int(input('Please enter your age.'))
cindy = int(input('Please enter the age of Cindy.'))
josh = int(input('Please enter the age of Josh.'))
avg = float(me+cindy+josh)/3
print("{:.2f}".format(avg))
