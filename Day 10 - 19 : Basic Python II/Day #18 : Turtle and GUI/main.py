import turtle as t
import random 

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape ("turtle") 
# timmy_the_turtle.color ("Red")

# for _ in range (4):
   # timmy_the_turtle.forward(180)
   # timmy_the_turtle.lef(90)


#Draw a dash line 

#tim = t.Turtle()

#def draw_shape(num_sides):
    #angel = 360/ num_sides 
   # for _ in range(15):
      #  tim.forward(10)
       # tim.pen()
       # tim.forward(10)
       # tim.pendown()

# Draw a random walk using rand.pensize, color

tim  = t.Turtle()

colours = ["cornflowerBlue", "DarkOrchid", "IndianRed"]
directions =  [9, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick(
)