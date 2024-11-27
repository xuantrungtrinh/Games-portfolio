from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# ==> put this in as a constant. So right at the top, and remember that in Python, the constants are named with all caps like this, and also with snake case with underscores separating each of the words.
# (0, 0), (-20, 0), (-40, 0) in this case are all TUPLES. Remember that!

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# ==> the reason why we have all these constants is so that if we wanted to tweak our game, say if we wanted the snake to start at a different position or for it to move further each time, then we don't have to dig through the body of our code. All we have to do is look at the top, look at all the things that we can change and then change it accordingly.

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # ==> Now, remember if you have this line of code above the create_snake, it's probably going to error out because at this point the segments is empty and if you try to get the first item from it, it's not going to allow you to.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # ==? Now be really careful here because it's not just self.head.heading, it's actually heading as a method because remember that the head of the snake is the first segment of our list of segments and each segment is a individual turtle. The turtle has a heading method which will give you a direction in terms of these 360-degree numbers, and then we can use that to check to see if it's equal to down. And if it is, then it's not allowed to go up.

    def down(self):
        # pass
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        # pass
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        # pass
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)









