import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)
		
def draw_art():
	window = turtle.Screen()
	window.bgcolor("green")

	#Create the turtle Brad - Draws a Square to make a flower
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(15)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	for i in range(37,38):		
		brad.left(90)
		brad.backward(350)

	window.exitonclick()

draw_art()