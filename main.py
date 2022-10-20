import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.goto(0,0)

screen = turtle.Screen()
screen.bgcolor("black")


target = turtle.Turtle()
target.speed(1000)
target.color("blue")
target.shape("circle")
target.penup()
target.goto(random.randint(-200,200), random.randint(-200,200))


def turnleft():
  t.left(10)

def turnright():
  t.right(10)


def shoot():
  bullet = turtle.Turtle()
  bullet.penup()
  bullet.color("yellow")
  bullet.speed(1000)
  bullet.setheading(t.heading())
  
  for i in range(300):
    bullet.forward(10)
    if bullet.xcor() > target.xcor()-10 and bullet.xcor() < target.xcor()+10 and bullet.ycor() > target.ycor()-10 and bullet.ycor() < target.ycor()+10:
      bullet.ht()
      target.goto(random.randint(-200,200), random.randint(-200,200))

screen.onkey(turnleft, "Left")
screen.onkey(turnright, "Right")
screen.onkey(shoot, "space")
screen.listen()
