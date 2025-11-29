import random
import turtle
import time
turtle.speed(100)
turtle.hideturtle()
for a in range(random.randint(10,50)):
    time.sleep(1)
    turtle.clear()
    turtle.up()
    turtle.goto(random.randint(10,50),random.randint(10,50))
    turtle.down()
    ku = random.randint(20,250)
    renk = ["red","green","blue"]
    turtle.color(random.choice(renk))
    for a in range(4):
        turtle.forward(ku)
        turtle.right(90)


input()
