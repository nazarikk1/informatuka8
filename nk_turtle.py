from turtle import *

color('lightblue')
width(10)
speed(10)

for x in range(1, 100, 4):
    forward(x)
    left(90)
    
color('white')

penup()
goto(-30, -20)
pendown()
write("Н", font=("Arial", 30, "bold"))

penup()
goto(0, -20)
pendown()
write("К", font=("Arial", 30, "bold"))

hideturtle()

done()
