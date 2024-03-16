import turtle
from random import randint
import time
FONT = ("Arial", 20, "normal")
score = 0
zaman = 30

''''
for i in range(30):
    zaman = zaman - 1

def clicking():
    pass
'''

#screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

#Text
top_heigh = screen.window_height()/2
y = top_heigh - top_heigh/10

txt = turtle.Turtle()
txt.penup()
txt.hideturtle()
txt.setposition(0, y)
txt.write(f"Kalan Zaman: {zaman}", align="center",  font=FONT)

txt2 = turtle.Turtle()
txt2.penup()
txt2.hideturtle()
txt2.setposition(0, y-25)
txt2.write(f"Score: {score}", align="center", font=FONT)


#turtle icon
turtle_icon = turtle.Turtle()
turtle_icon.shape("turtle")
turtle_icon.shapesize(2)
turtle_icon.color("green")

for i in range(5):
    turtle_icon.penup()
    turtle_icon.hideturtle()
    turtle_icon.goto(randint(0,300), randint(0,300))
    turtle_icon.showturtle()
    time.sleep(0.80)


turtle.mainloop()