import turtle
import time
from random import randint

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
screen.listen()

FONT = ("Arial", 20, "normal")
score = 0
countdown = 10

class Genel():

    def __init__(self):
        self.turtle_icon = turtle.Turtle()
        self.turtle_icon.shape("turtle")
        self.turtle_icon.pensize(2)
        self.turtle_icon.color("green")

        top_heigh = screen.window_height() / 2
        y = top_heigh - top_heigh / 10

        self.txt = turtle.Turtle()
        self.txt.penup()
        self.txt.hideturtle()
        self.txt.setposition(0, y)
        self.txt.write(f"Kalan Zaman: {countdown}", align="center", font=FONT)

        self.txt2 = turtle.Turtle()
        self.txt2.penup()
        self.txt2.hideturtle()
        self.txt2.setposition(0, y - 25)
        self.txt2.write(f"Score: {score}", align="center", font=FONT)

        for i in range(countdown, -1, -1):

            def clicking():
                self.txt2.clear()
                self.txt2.write(f"Score: {score + 1}", align="center", font=FONT)

            self.turtle_icon.penup()
            self.turtle_icon.hideturtle()
            self.turtle_icon.goto(randint(0, 300), randint(0, 300))
            self.turtle_icon.showturtle()
            self.turtle_icon.onclick(clicking)
            self.txt.clear()
            self.txt.write(f"Kalan Zaman: {i}", align="center", font=FONT)
            time.sleep(0.80)

            if i == 0:
                self.txt.clear()
                self.txt.write("Game Over", align="center", font=FONT)

Genel()
turtle.mainloop()
