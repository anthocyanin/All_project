import turtle

# 初始化
pen = turtle.Pen()
turtle.colormode(255)
turtle.setup(840, 500)  # 设置主窗口的大小
turtle.title('小猪佩奇')
pen.pensize(4)
pen.hideturtle()
pen.speed(9)
pen.color('pink')

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(180)
pen.circle(-100, 180)  # 画圆是这样的步骤。第一步在哪个点开始画，画多大的半径的圆，根据前面的setheading(角度)自动计算出圆心，然后问你要哪一块。
# pen.color('blue')
# pen.circle(100, -60)
# pen.color('red')
# pen.circle(80, -100)
# pen.color('green')
# pen.circle(150, -20)
# pen.color('black')
# pen.circle(60, -95)

turtle.done()

