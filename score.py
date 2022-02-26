from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.sleep_time = 0.1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Level: {self.level} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()
        self.increase_level()

    def increase_level(self):
        if self.score % 5 == 0:
            self.level += 1
            self.clear()
            self.update_scoreboard()
            self.increase_speed()

    def increase_speed(self):
        if self.level % 5 == 0:
            self.sleep_time *= 0.9
            if self.sleep_time == 0.02:
                self.sleep_time = 0.02

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as score:
                score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     # self.clear()
    #     self.write("GAME OVER 😔", align=ALIGNMENT, font=FONT)

    def game_won(self):
        if self.level == 100:
            self.goto(0, 0)
            self.write("You Won 🎉", align=ALIGNMENT, font=FONT)
            return True
