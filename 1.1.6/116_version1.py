#   a116_buggarm_image.parm
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
bug = trtl.Turtle()
bug.pensize(40)
bug.circle(20)
leg = 6
arm = 70
antena = 380 / leg
bug.pensize(5)
n = 0
while (n < leg):
  bug.goto(0,0)
  bug.setheading(antena*n)
  bug.forward(arm)
  n = n + 1
bug.hideturtle()
wn = trtl.Screen()
wn.mainloop()