# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 10/10/2022
# Date of Submission: 10/10/2022
# Description: Ingredient tell-er.
# Input: Cookies wanted.
# Output: Ingredients needed.
# Additional Comments: V 1.0

cookies = int(input("How many cookies do you want?"))
sugar = (cookies/48)*1.5
butter = (cookies/48)*1
flour = (cookies/48)*2.75
print("You need "+str(("{:.2f}".format(sugar)))+" "+str(("{:.2f}".format(butter)))+" cups of butter," " and " +str(("{:.2f}".format(flour)))+" cups of flour.")
