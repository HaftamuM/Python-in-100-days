#subject cover : inheitance 
from turtle import Turtle

class Food(Turtle): 

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pennup()
        self.shapesize(strech_len=0.5, strech_width=0.5)
        self.color("Blue")
        self.speed("fastest")
        random_x = random.randint(-290, 288)
        random_y = random.randint(-288, 288)
        self.goto(random_x, random_y)
        