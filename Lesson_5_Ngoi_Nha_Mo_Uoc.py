import turtle
import tkinter

screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor('#87ceeb')
pen=turtle.Turtle()
pen.pensize(3)
pen.color('black')

# LOCATION OF HOUSE
pen.penup()
pen.goto(-245,105)
pen.write('House',font=('Times new Roman','20','bold'))

# Paint Blue Wall:
pen.penup()
pen.goto(-258,-210)
pen.pendown()
pen.fillcolor('blue')
pen.begin_fill()
pen.fd(162)
pen.left(90)
pen.fd(180)
pen.left(90)
pen.fd(162)
pen.left(90)
pen.fd(180)
pen.left(90)
pen.end_fill()
pen.penup()

# Paint Green Door:
pen.penup()
pen.goto(-210,-210)
pen.pendown()
pen.fillcolor('#91f190')
pen.begin_fill()
pen.fd(66)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(66)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.end_fill()
pen.penup()

# Paint Triangle Roof:
pen.penup()
pen.goto(-96,-30)
pen.pendown()
pen.fillcolor('#fe01fd')
pen.begin_fill()
pen.left(135)
pen.fd(114)
pen.left(90)
pen.fd(114)
pen.end_fill()
pen.penup()

# Paint Yellow Wall:
pen.penup()
pen.goto(-96,-210)
pen.pendown()
pen.fillcolor('#feff02')
pen.begin_fill()
pen.goto((-10,-160))
pen.goto((-10,22))
pen.goto((-96,-30))
pen.goto((-96,-210))
pen.end_fill()
pen.penup()

# Paint Orange Roof:
pen.penup()
pen.goto(-96,-30)
pen.pendown()
pen.fillcolor('#ffa500')
pen.begin_fill()
pen.goto((-10,22))
pen.goto((-90,105))
pen.goto((-177,51))
pen.goto((-96,-30))
pen.end_fill()
pen.penup()

# Paint Brown Windows:
pen.penup()
pen.goto(-66,-110)
pen.pendown()
pen.fillcolor('#a62a2a')
pen.begin_fill()
pen.goto((-33,-93))
pen.goto((-33,-45))
pen.goto((-66,-63))
pen.goto((-66,-110))
pen.end_fill()
pen.penup()

# LOCATION OF TREE
pen.penup()
pen.goto(220,-240)
pen.write('Tree',font=('Times new Roman','20','bold'))

# Paint Brown Trunk Of Tree:
pen.penup()
pen.goto(150,-225)
pen.pendown()
pen.fillcolor('#a62a2a')
pen.begin_fill()
pen.goto((185,-225))
pen.goto((185,-160))
pen.goto((150,-160))
pen.goto((150,-225))
pen.end_fill()
pen.penup()

# Paint Green Top Of Tree (1/3):
pen.penup()
pen.goto(93,-160)
pen.pendown()
pen.fillcolor('#91f190')
pen.begin_fill()
pen.goto((242,-160))
pen.goto((168,-85))
pen.goto((93,-160))
pen.end_fill()
pen.penup()

# Paint Green Top Of Tree (2/3):
pen.penup()
pen.goto(102,-87)
pen.pendown()
pen.fillcolor('#91f190')
pen.begin_fill()
pen.goto((233,-87))
pen.goto((168,-19))
pen.goto((102,-87))
pen.end_fill()
pen.penup()

# Paint Green Top Of Tree (3/3):
pen.penup()
pen.goto(111,-21)
pen.pendown()
pen.fillcolor('#91f190')
pen.begin_fill()
pen.goto((224,-21))
pen.goto((168,36))
pen.goto((111,-21))
pen.end_fill()
pen.penup()

# LOCATION OF SUN
pen.penup()
pen.goto(180,230)
pen.write('Sun',font=('Times new Roman','20','bold'))

# Paint Sunshine:
pen.penup()
pen.goto(-4,207)
pen.pendown()
pen.goto(156,207)
pen.penup()
pen.goto(76,287)
pen.pendown()
pen.goto(76,127)
pen.penup()
pen.goto(33,252)
pen.pendown()
pen.goto(120,162)
pen.penup()
pen.goto(120,252)
pen.pendown()
pen.goto(33,162)
pen.penup()

# Paint Yellow Sun:
pen.penup()
pen.goto(51,232)
pen.fillcolor('#feff02')
pen.begin_fill()
pen.pendown()
pen.circle(36)
pen.end_fill()
pen.penup()

# LOCATION OF TURTLE GOING HOME
pen.penup()
pen.goto(-180,-255)
pen.penup
pen.right(135)
pen.color('black')
pen.fillcolor('black')
pen.shape('turtle')
for i in range(1,10):
    pen.goto(-180,-265)
    turtle.delay(100)  
    pen.goto(-180,-260)
    turtle.delay(100)  
    pen.goto(-180,-255)
    turtle.delay(100)
    pen.goto(-180,-245)
    turtle.delay(100)
    pen.goto(-180,-240)

tkinter.mainloop()

# B??i l??m c???a em h??i lan man 200 d??ng code python
# Mu???n l???p m??nh t???t c??? ch??ng ta c??ng c??? g???ng nh?? 