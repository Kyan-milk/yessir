#members: Giselle, Carlese, Kyan, Jane

import turtle as trtl

t = trtl.Turtle()
t.speed(0)

#User Input
equation=input("y=mx+b: ")
variable_m = int(equation[2])
variable_b = int(equation[5])

 # axis function
def create_axis():
  t.penup()
  t.goto(-100, 0)
  t.pendown()
  t.forward(200)
  t.penup()
  t.goto(0, -100)
  t.left(90)
  t.pendown()
  t.forward(200)
  t.right(90)

# calling function
create_axis() 

#creating hashmarks
t.penup()
t.setposition(-100,0)
t.pendown()
for x in range(40):
  t.left(90)
  t.forward(5)
  t.right(180)
  t.forward(10)
  t.right(180)
  t.forward(5)
  t.right(90)
  t.forward(5)    

t.penup()
t.goto(0,-100)
t.pendown()

for x in range(40):
  t.forward(5)
  t.right(180)
  t.forward(10)
  t.right(180)
  t.forward(5)
  t.left(90)
  t.forward(5)
  t.right(90)

#creating line function
t.color("red")
t.pensize(1)
m = variable_m*5
b = variable_b*5
def draw_line():
  t.penup()
  left_y = int(m*-100+b)
  right_y = int(m*100+b)
  t.goto(-100,left_y)
  t.pendown()
  t.goto(100,right_y)

#calling line function
draw_line()

wn=trtl.Screen ()
wn.mainloop ()