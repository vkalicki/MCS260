#MSC 260 Project 3 by Veronica Kalicki
import turtle
import random
import math

randx = [-160, -80, 0, 80, 160]

speed = 0

mallet = ()

#This creates the screen
wm = turtle.Screen()


holes = []  #list where hole cords are hidden
totalholes = 150

newX = -160
newY = -160
count = 0

for num1 in range(5):
    for num2 in range(5):
        holes.append(turtle.Turtle())
        holes[count].color("Black")
        holes[count].shape("circle")
        holes[count].penup()
        holes[count].speed(0)
        holes[count].setposition(newX, newY)
        newX += 80
        count += 1
    newX = -160
    newY += 80

moles = []   #moles list

for count in range(9):
        moles.append(turtle.Turtle())  # attach mole to list
        moles[count].color("Red")  # moles color
        moles[count].shape("circle")  # moles shape
        moles[count].penup()  # moles dont draw
        moles[count].speed(0)  # moles dont move
        moles[count].setposition(random.choice(randx), random.choice(randx))  # moles get randomly placed

#Creates our mallet
mallet = turtle.Turtle()
mallet.shape("circle")  # assigns shape
mallet.color("blue")  # assigns color
mallet.penup()  # makes it not mark down lines
mallet.setposition(0, 0)  # centers mallet at start


#keyboard controls

def move_left():  # moves mallet left
    x = mallet.xcor()
    x -= 80
    if x < -160:  # border check
        x = -160
    mallet.setx(x)


def move_right():  # moves mallet right
    x = mallet.xcor()
    x += 80
    if x > 160:  # border check
        x = 160
    mallet.setx(x)


def up():  # moves mallet up
    y = mallet.ycor()
    y += 80
    if y > 160:  # border check
        y = 160
    mallet.sety(y)


def down(): # moves mallet down
    y = mallet.ycor()
    y -= 80
    if y < -160:  # border check
        y = -160
    mallet.sety(y)

# Create Keyboard Bindings
turtle.listen()   # has the program respond to keys
turtle.onkey(move_left, "Left")  # left arrow
turtle.onkey(move_right, "Right")  # right arrow
turtle.onkey(up, "Up")  # up arrow
turtle.onkey(down, "Down")  # down arrow


def collide(t1, t2):  # collision Definition
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

while True:
    mallet.forward(speed)

    for count in range(9):
        if collide(mallet, moles[count]):
            moles[count].setposition(random.choice(randx), random.choice(randx))  # moves the collided moles

    turtle.mainloop()
