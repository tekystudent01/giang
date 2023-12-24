import random
import turtle 
screen = turtle.Screen()


screen.bgpic('anh-nen-giang-sinh.gif')



myPen= turtle.Turtle()
myPen.speed(4000)
myPen.pensize(3)


def addText(message, color, x, y, size):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    style = ('Courier', size , 'italic')
    myPen.write(message, font=style, align= 'center')


addText('Happy merry christmas', '#FF0000',0,0,30)
addText('With your friends and family','#FFFFFF', 0,-30,15)

def hoatuyet():
    myPen.penup()
    myPen.goto(random.randint(-300,300),random.randint(-300,300))
    myPen.pendown()
    for i in range (0,8):

        myPen.forward(50)
        myPen.penup()
        myPen.backward(15)
        myPen.left(45)
        myPen.pendown()
        myPen.forward(5)
        myPen.backward(5)
        myPen.right(90)
        myPen.forward(5)
        myPen.backward(5)
        myPen.left(45)
        myPen.backward(35)
        myPen.left(45)

for i in range (0, 8):
    hoatuyet()


    
screen.update()
screen.exitonclick()