import turtle

typer = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

typer.penup()

for y in range(height):
	for i in range(width):
		typer.dot()
		typer.forward(dot_distance)
	typer.backward(dot_distance*width)
	typer.right(90)
	typer.forward(dot_distance)
	typer.left(90)

turtle.done()