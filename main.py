from turtle import Screen
import time
from Snake import snake
from food import Food
from scoreboard import Scoreboard
scr=Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("The snake game")
scr.tracer(0)
# creating game objects

s = snake()
f = Food()
board = Scoreboard()

scr.listen()
scr.onkey(s.up, "Up")
scr.onkey(s.down, "Down")
scr.onkey(s.left, "Left")
scr.onkey(s.right, "Right")


game_on = True
while game_on:
    scr.update()
    time.sleep(0.5)
    s.move()
    if s.head.distance(f)<15:
        f.newwpos()
        s.extend()
        board.inc_score()

    if s.head.xcor() > 290 or s.head.xcor() < -290 or s.head.ycor() > 290 or s.head.ycor() < -290:
        game_is_on = False
        board.game_over()

    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            game_is_on = False
            board.game_over()

scr.exitonclick()

