import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_helena():
    turtle.color("blue")
    astamp = turtle.stamp()
    turtle.fd(50)
    turtle.position()
(200.00,-0.00)
    turtle.clearstamp(astamp)
    turtle.position()
(200.00,-0.00)
       
    
    for i in range(1,38):
        for i in range(1,5):
            turtle.forward(100)
            turtle.right(90)
        for i in range(1,2):
            turtle.right(10)
        
    window.exitonclick()    
     
draw_helena()
