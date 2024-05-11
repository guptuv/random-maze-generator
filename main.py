from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
x=-2000
while x!=2000:
    tim.color(random.choice(colours))
    direct=random.randint(1,2)
    if(direct==1):
        tim.forward(40)
        tim.setheading(random.choice(directions))
    else:
        tim.backward(40)
        tim.setheading(random.choice(directions))
    x=x+1
screen.exitonclick()
