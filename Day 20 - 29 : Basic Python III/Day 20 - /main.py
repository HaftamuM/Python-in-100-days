#create a snake class
#create a food
#create a scoreboard 

from turtle import screen, Turtle
from snake import Snake
from food import Food 
from scoreboard import Scoreboard
import time 
screen = screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-G")
screen.tracer(0)

# Create a snake body - which is the sum of screen block

#segment_1 = Turtle("square")
#segment_1.color("white")

#segment_2 = Turtle("square")
#segment_2.color("white")
#segment_2.goto(-20, 0)

#segment_3 = Turtle("square")
#segment_3.color("white")
#segment_3.goto(-40, 0)

# Create a snake body 


segments =  []


# Move the snake forward with a given time, and speed

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up") #snake up is triggerd 
screen.onkey(snake.down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


game_is_on = True 
while game_is_on: 
    screen.updat()
    time.sleep(0.1)
    snake.move()
     # one second delay 
    # for seg in segments: 
      #  seg.forwared(20)
    #Turn the segments in different direction , moving the third segment to the second, and the second to the 
    #first segment 
    #control the snake using the keyboard - key biding 
    #Detect collision with food , using distance method
    if snake.head.distance(food) < 15:
        print("collided")
        food.refresh()
        scoreboard.increase_score()
        
screen.exitonclick()