from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


l_paddle = Paddle("left")
r_paddle = Paddle("right")
# screen.update()


# paddle()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

def stop_game(x = 5, y = 3):
    global game_is_on
    game_is_on = False

screen.onclick(stop_game)

while game_is_on:
    screen.update()

