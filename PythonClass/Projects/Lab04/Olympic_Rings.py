# ITP-100 Software Design
# Student: Jeannotte, Michael
# Instructor: Brown, Georgia
# Date given to class: 9-12-2022
# Date of Submission:
# Description:
# Input:
# Output:
# Additional Comments: V 1.0

import turtle

# object tr for turtle
turt = turtle.Turtle()
turt.pensize(5)
turt.speed(5)

turt.color("blue")
turt.penup()
turt.goto(-110, -25)
turt.pendown()
turt.circle(45)

turt.color("black")
turt.penup()
turt.goto(0, -25)
turt.pendown()
turt.circle(45)

turt.color("red")
turt.penup()
turt.goto(110, -25)
turt.pendown()
turt.circle(45)

turt.color("yellow")
turt.penup()
turt.goto(-55, -75)
turt.pendown()
turt.circle(45)

turt.color("green")
turt.penup()
turt.goto(55, -75)
turt.pendown()
turt.circle(45)
turt.penup()

turtle.done()