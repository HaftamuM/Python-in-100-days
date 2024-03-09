from turtle import screen, Turtle

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
starting_positions = [(0, 0), (-20, 0), (-40, 0)] # how tuples works 

segments =  []
for position in starting_positions: 
    new_segment = Turtle("Square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Move the snake forward with a given time, and speed
game_is_on = True 
while game_is_on: 
    screen.updat()
    time.sleep(0.1) # one second delay 
    # for seg in segments: 
      #  seg.forwared(20)
#Turn the segments in different direction , moving the third segment to the second, and the second to the 
#first segment 
    
    for seg_num in range(len(segments)-1 , 0 , -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y) 
    segments[0].forward(20)

screen.exitonclick()