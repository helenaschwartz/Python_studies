import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create Turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #Create Turtle Angie - draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    #Create Turtle Trian - draws a triangle
    trian = turtle.Turtle()
    trian.shape("square")
    trian.color("green")
    draw_triangle(trian)
   
    window.exitonclick()    

draw_art()  
