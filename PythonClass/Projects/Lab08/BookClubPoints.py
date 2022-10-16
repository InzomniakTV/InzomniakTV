# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 10/10/2022
# Date of Submission: 10/10/2022
# Description: Average out ages.
# Input: 3 persons' age.
# Output: Average age of the 3 people.
# Additional Comments: V 1.0
# 11. Book Club Points MJ
#
# Serendipity Booksellers has a book club that awards points
# to its customers based on the number of books purchased each
# month. The points are awarded as follows:
#
# • If a customer purchases 0 books, he or she earns 0 points.
# • If a customer purchases 2 books, he or she earns 5 points.
# • If a customer purchases 4 books, he or she earns 15 points.
# • If a customer purchases 6 books, he or she earns 30 points.
# • If a customer purchases 8 or more books, he or she earns 60 points.
#
# Write a program that asks the user to enter the number of books
# that he or she has purchased this month, then displays the number of points awarded.
#
number_of_books = int(input("Enter the number of books: "))
message = ""

if number_of_books < 0:
    message = "Error. Enter a positive number. \n" + \
              "Re-run program and try again."
else:
    message = "You are awared "

    if number_of_books >= 0 and number_of_books <= 1:
        message += "0 "
    elif number_of_books >= 2 and number_of_books <= 3:
        message += "5 "
    elif number_of_books >= 4 and number_of_books <= 5:
        message += "15 "
    elif number_of_books >= 6 and number_of_books <= 7:
        message += "30 "
    elif number_of_books >= 8:
        message += "60 "

    message += "points."

print(message)
