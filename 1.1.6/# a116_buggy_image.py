#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
bug = trtl.Turtle()
bug.pensize(40)
bug.circle(20)
leg = 6
y = 70
z = 380 / leg
bug.pensize(5)
n = 0
while (n < leg):
  bug.goto(0,0)
  bug.setheading(z*n)
  bug.forward(y)
  n = n + 1
bug.hideturtle()
wn = trtl.Screen()
wn.mainloop()