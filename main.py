from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# setting up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game 🐍")
screen.tracer(0)

# getting snake and food to appear on screen
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# getting snake to respond to keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "Left")

# sleep_time = 0.02
# playing game
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(scoreboard.sleep_time)
    snake.move()

    # detecting if the snake has eaten food
    if snake.head.distance(food) < 15:
        food.place_food()
        snake.increase_length()
        scoreboard.increase_score()

    # detecting if the snake has ran into wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.level = 1
        scoreboard.reset_score()
        snake.reset_snake()

    # Detecting if the snake has hit its body
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.level = 1
            scoreboard.reset_score()
            snake.reset_snake()

    if scoreboard.game_won():
        is_game_on = False

screen.exitonclick()
