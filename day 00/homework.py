from turtle import*

#we want to draw a house

#step1: draw a square
 
color("purple")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#end of a square

#drawing a dor

left(90)
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

#end of a dor

#drawing a window

color("purple")
left(90)
forward(70)
left(90)
forward(80)
color("green")
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
goto(0,0)
pendown()
color("purple")
left(90)
forward(80)
color("green")
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


#end of a window

#drawing a roof
penup()
goto(200,200)
pendown()
right(60)
forward(200)
left(120)
forward(200)

exitonclick()