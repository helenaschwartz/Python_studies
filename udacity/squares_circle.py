import turtle

def draw_square(some_turtle):
    for i in range(1,38):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        for i in range(1,2):
            some_turtle.right(10)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create Turtle Brad - draws a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(12)
    draw_square(brad)

    window.exitonclick()    
     
draw_art()
