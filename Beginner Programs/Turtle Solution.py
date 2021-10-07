from turtle import *


color('red')
penup()
forward(227.26)
FIRST_POS = pos()
pendown()
speed("fastest")
left(30)
while True:
    forward(20)
    left(120)
    forward(20)
    right(115)
    if abs(pos()-FIRST_POS) < 1:
        break
penup()
done()
