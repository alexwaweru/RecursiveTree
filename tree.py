import turtle
import random

def tree(branch_len, t, width, g):
    t.speed(1000) #Speed of the turtle
    t.pensize(width)
    t.pencolor(0,g,0)
    if branch_len > 5:
        t.forward(branch_len)
        angle = random.randint(15,45)
        t.right(angle)
        tree(branch_len - random.randint(10,20), t, width*(3/4),float(g)*1.2)
        t.left(angle*2)
        tree(branch_len - random.randint(10,20), t, width*(3/4),float(g)*1.2)
        t.right(angle)
        t.backward(branch_len)
        
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(250)
    t.down()
    #t.color("green")
    tree(110, t, 10, 40/255)
    my_win.exitonclick()
    
main()
