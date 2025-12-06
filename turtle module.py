#turtle
import turtle
'''fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(90)
fred.forward(100)
fred.right(90)
fred.forward(100)
fred.right(90)
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.left(135) #change this value for different shapes
fred.forward(100)
fred.left(135)
fred.forward(140)

amy = turtle.Turtle()
amy.color("green")
for i in range(5):
    amy.forward(100)
    amy.right(90)
    amy.backward(120)
    amy.left(90)
#3 Quarter PI filled with grey
amy = turtle.Turtle()
amy.color("blue")
amy.fillcolor("orange")
amy.circle(-100,90)
amy.right(90)
amy.forward(100)
amy.left(90)
amy.backward(100)

#4 Pie chart with 4 slices
import turtle

t = turtle.Turtle()
t.speed(2)

# Values for the pie chart
slices = [20, 35, 25, 25]
colors = ["red", "blue", "green", "yellow"]

total = sum(slices)

for i, value in enumerate(slices):
    angle = (value / total) * 360  # convert value to degrees
    
    t.fillcolor(colors[i])
    t.begin_fill()
    
    t.forward(100)     # radius
    t.circle(90, angle)
    t.right(180 - angle)
    t.forward(90)
    
    t.end_fill()
    t.left(90)
    
turtle.done()'''
#5 Draw Pentagon , hexagon, star









