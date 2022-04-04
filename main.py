from turtle import Turtle, Screen
import random

angelo = Turtle()
angelo.shape("turtle")
angelo.color("DarkGoldenrod1")
angelo.pencolor("DeepPink3")
angelo.width(1)
angelo.speed("fastest")

colors = ["PeachPuff", "LightSalmon", "Coral", "Tomato", "OrangeRed", "Red",
          "indian red", "Crimson","DarkSalmon",]
directions = [0, 90, 180, 270]

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        angelo.color(random.choice(colors))
        angelo.circle(100)
        angelo.setheading(angelo.heading()+size_of_gap)

draw_spirograph(5)




#for i in range(300):
    #angelo.forward(30)
    #angelo.color(random.choice(colors))
    #angelo.setheading(random.choice(directions))


#def draw_shape(num_sides):
    #angle = 360 / num_sides
    #for _ in range(num_sides):
        #angelo.forward(100)
       # angelo.right(angle)

#for draw_shape_n in range(3, 11):
    #angelo.color(random.choice(colors))
    #draw_shape(draw_shape_n)


screen = Screen()
screen.exitonclick()