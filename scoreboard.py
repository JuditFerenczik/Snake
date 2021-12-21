from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as high_score:
            previous_score = high_score.read()
            self.high_score = int(previous_score)
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score:  {self.score}",align=ALLIGNMENT,font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}. High score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()