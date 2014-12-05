import turtle

def draw_forms():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    trian = turtle.Turtle()
    trian.shape("square")
    trian.color("green")

    trian.forward(100)
    trian.right(120)
    trian.forward(100)
    trian.right(120)
    trian.forward(100)
    
    window.exitonclick()    

draw_forms()  
