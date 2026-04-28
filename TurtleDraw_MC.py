print("Start Turtle Draw!")
import turtle 
screen = turtle.Screen()
screen.setup(width=450, height=450)
t = turtle.Turtle()


edTheTurtle = turtle.Turtle()
edTheTurtle.forward(100)

turtle.done()


spiral = turtle.Turtle()
spiral.pencolor("purple")
for i in range(40):
    spiral.forward(i * 10)
    spiral.rght(144)
  '''

print('Reading a text file line by line.')
TurtleDraw = open(TEXTFILENAME, 'r')
Line = TurtleDraw.readline()

while line:
    print(line, end='')
  line = turtleDraw

  if(len(parts) == 3):
  color = parts[0]
  x = int(parts[1])
  y = int(parts[2])


  TurtleDraw.color(color)
  TurtleDraw.goto(x,y)
  TurtleDraw.pendown()


  draw.pendown()
  draw.goto(x,y)

  Line = TurtleDraw.readline()

  turtle.done()

  #Wait to press the enter key button
  print('\nEnd')
