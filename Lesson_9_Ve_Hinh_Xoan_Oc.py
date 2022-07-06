import turtle
import tkinter

d0=int(input('Nhap khoang cach toi da (100-300): '))
screen=turtle.Screen()
screen.setup(800,800)
screen.title('Ve hinh xoan oc')
screen.bgcolor('gray')
pen=turtle.Turtle()
pen.pensize(2)
pen.color('black')
pen.penup()
pen.goto(0,0)
pen.speed(0)
pen.pendown()
for i in range(1,1000):
    pen.left(10)
    pen.fd(1+0.1*i)
    d1=turtle.distance(pen)
    if d1>=d0:
        break
tkinter.mainloop()
