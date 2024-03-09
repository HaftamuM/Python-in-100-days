#https://www.freecodecamp.org/news/how-to-make-racing-game-using-python/
#Add the pictures and more 
# creating differnet object from a class.. which a class is variable
#timmy = Turtle() - instance 
#tommy = Turtle() - instance 
#The state of different  objects .. are different 

from turtle import Turtle, screen 

time = Turtle()
screen = Screen()

#def mov_forwards():
#    tim.forward(10)

#def mov_backwards():
#    tim.forward(10)

#def turn_left():
  #  new_heading = tim.heading() + 10
 #   tim.setheading(new_heading)

#def turn_right():
    #new_heading = tim.heading() - 10
   # tim.setheading(new_heading)

#def clear(): 
    #tim.clear()
   # tim.penup()
  #  tim.home()
 #   tim.pendown()


#screen.listen()
#screen.onkey(move_forwards, "w")
#screen.onkey(move_backwards, "s")
#screen.onkey(move_left, "a")
#screen.onkey(turn_right, "d")
#screen.onkey(clear, "c")
screen.set(widt=500, height=400 )
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the reace? Enter a color:")
colors = ["red", "orange","yellow", "green", "blue", "blue", "Purple"]
all_turtles = []


y_positions = [-70, -40, -10, 20, 50,80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
#ramdom moveing 
    
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()  > 230: 
            is_race_on = False 
            wining_color = turtle.pencolor()
            if wining_color == user_bet: 
                print(f"You have won! The {winning_color} turtle is the wineer!")
            else: 
                print(f"You have lost! The {winning_color} turtle is the winner!")
            


        rand_distance = random.randin(0, 10)
        turtle.forward(rand_distnace)

screen.exitonclick()

