import turtle
import random
FONT = ("Arial", 20, "normal")

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
txt.write("Kalan Zaman:", align="center",  font=FONT)

txt2 = turtle.Turtle()
txt2.penup()
txt2.hideturtle()
txt2.setposition(0, y-25)
txt2.write("Score:", align="center", font=FONT)


#turtle icon
turtle_icon = turtle.Turtle()
turtle_icon.shape("turtle")
turtle_icon.shapesize(3)
turtle_icon.color("green")

turtle.mainloop()