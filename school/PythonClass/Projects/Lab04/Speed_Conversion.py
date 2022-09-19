# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 9-12-2022
# Date of Submission:
# Description: Conversions of KPH to MPH in increments of 10
# Input: None
# Output: Conversions of KPH to MPH in increments of 10
# Additional Comments: V 2.0

START_SPEED = 60 # Starting speed
END_SPEED = 131 # Ending speed
INCREMENT = 10 # Speed increment
CONVERSION_FACTOR = 0.6214 # Conversion factor
MAX_SPEED = 500 # Just testing this.

# Prints the table headings above the conversions.
print('KPH\tMPH')
print('--------------')

# Prints the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT) :
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')

print('MORE!')

# Let's add some more!
for kph in range(END_SPEED, MAX_SPEED, INCREMENT) :
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')
