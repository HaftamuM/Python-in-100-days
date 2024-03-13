from turtle import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # how tuples works 
UP = 90
Down = 270
Left = 180
Right = 0
class Snake: 
    def __init__(self): #intalizaing the class 
        self.segments = [] 
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS: 
            new_segment = Turtle("Square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def mov(self):
        for seg_num in range(len(self.segments)-1 , 0 , -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y) 
        self.head.segments[0].forward(20)

    def up(self):
        if self.head.heading() != Down:
            self.segments[0].setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.jead.setheading(270)
    def left(self):
        if self.head.heading() != Right: 
            self.jead.setheading(180)
    def right(self):
        if self.head.heading() != Left: 
            self.jead.setheading(0)