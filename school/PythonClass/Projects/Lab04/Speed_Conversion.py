# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 9-12-2022
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments: V 1.0

START_SPEED = 60 # Starting speed
END_SPEED = 131 # Ending speed
INCREMENT = 10 # Speed increment
CONVERSION_FACTOR = 0.6214 # Conversion factor

# Print the table headings.
print('KPH\tMPH')
print('--------------')

# Print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT)
mph = kph * CONVERSION_FACTOR
print()rint(f'{kph}\t{mph:.1f}')