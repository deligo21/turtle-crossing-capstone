from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :P", False, 'center', FONT)
