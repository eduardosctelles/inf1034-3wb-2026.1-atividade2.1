from turtle import *

t = Turtle()
for i in range(3):
    t.forward(300)
    t.stamp()
    t.backward(300)
    t.right(90)

t.forward(300)
t.stamp()

t.penup()
t.goto(200,100)
t.pendown()

color = textinput("Qual cor você deseja pintar o triangulo", "?")
t.color(color)
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-200,100)
t.pendown()

color = textinput("Qual cor você deseja pintar o quadrado", "?")
t.color(color)
t.begin_fill()
t.left(90)
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-200,-100)
t.pendown()

color = textinput("Qual cor você deseja pintar o triangulo isóceles", "?")
t.color(color)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(120)
t.end_fill()

t.penup()
t.goto(200,-100)
t.pendown()

color = textinput("Qual cor você deseja pintar o octógono", "?")
t.color(color)
t.begin_fill()
for i in range(6):
    t.forward(50)
    t.left(60)
t.end_fill()

mainloop()