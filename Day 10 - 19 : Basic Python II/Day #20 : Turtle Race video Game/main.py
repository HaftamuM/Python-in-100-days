#https://www.freecodecamp.org/news/how-to-make-racing-game-using-python/
#Add the pictures and more 


from turtle import Turtle, screen 

time = Turtle()
screen = Screen()

def mov_forwards():
    tim.forward(10)

def mov_backwards():
    tim.forward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clea() 
    
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

