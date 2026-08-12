from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.starting_position = [(0, 0), (0, -20), (0, -40), (0, -60), (0, -80)]
        self.creat_snake()

    def creat_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=350, y=0)
        self.segments.append(new_segment)