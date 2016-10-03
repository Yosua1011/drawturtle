import turtle

def draw_rhombus(some_turtle,length,angle):
	for i in range(1,3):
		some_turtle.forward(length)
		some_turtle.left(180-angle)
		some_turtle.forward(length)
		some_turtle.left(angle)

def draw_shapes():
	
	window = turtle.Screen()
	window.bgcolor("white")

	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("blue")
	brad.speed(30)

	for i in range(1,73):
		draw_rhombus(brad,100,140)
		brad.right(10)

	brad.right(90)
	brad.forward(300)
		
	brad.right(145)
	draw_rhombus(brad,150,140)
		
	brad.right(110)
	draw_rhombus(brad,150,140)

	brad.hideturtle()

	window.exitonclick()

draw_shapes()