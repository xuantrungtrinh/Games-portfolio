from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(7.0, 1.0, 1)
        self.resizemode("user")
        self.penup()
        self.setposition(350,0)

    # def __call__(self):
    #     pass


# paddle = Paddle()

