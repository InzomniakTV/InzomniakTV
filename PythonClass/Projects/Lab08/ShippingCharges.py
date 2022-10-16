# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 10/10/2022
# Date of Submission: 10/10/2022
# Description: Average out ages.
# Input: 3 persons' age.
# Output: Average age of the 3 people.
# Additional Comments: V 1.0



weight_of_package = float(input("Enter weight of package: "))
shipping_charges = 0.0

message = "Shipping charges = "

if weight_of_package <= 2:
    shipping_charges = weight_of_package * 1.50
elif weight_of_package > 2 and weight_of_package <= 6:
    shipping_charges = weight_of_package * 3.00
elif weight_of_package > 6 and weight_of_package <= 10:
    shipping_charges = weight_of_package * 4.00
elif weight_of_package > 10:
    shipping_charges = weight_of_package * 4.75

message += "$" + format(shipping_charges, ',.2f')

print(message)
