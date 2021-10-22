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

# 鼻子
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.setheading(-30)  # 也写t.seth, 改变当前turtle的行进方向，angle为绝对角度
pen.begin_fill()
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        pen.lt(3)
        pen.forward(a)
    else:
        a = a - 0.08
        pen.lt(3)
        pen.forward(a)
        pen.end_fill()

# 左鼻孔
pen.penup()
pen.setheading(90)
pen.forward(25)
pen.setheading(0)
pen.forward(10)
pen.pendown()
pen.pencolor(255, 155, 192)
pen.setheading(10)
pen.begin_fill()
pen.circle(5)
pen.color(160, 82, 45)
pen.end_fill()

# 右鼻孔
pen.penup()
pen.setheading(0)
pen.forward(20)
pen.pendown()
pen.color(255, 155, 192)
pen.setheading(10)
pen.begin_fill()
pen.circle(5)
pen.color(160, 82, 45)
pen.end_fill()

# 绘制头的轮廓
pen.color((255, 155, 192), 'pink')
pen.penup()
pen.setheading(90)
pen.forward(41)
pen.setheading(0)
pen.forward(0)
pen.pendown()
pen.begin_fill()
pen.setheading(180)
pen.circle(300, -30)
pen.circle(100, -60)
pen.circle(80, -100)
pen.circle(150, -20)
pen.circle(60, -95)
pen.setheading(161)  # 所以这里就明白什么意思了
pen.circle(-300, 15)
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.setheading(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        pen.lt(3)
        pen.forward(a)
    else:
        a = a - 0.08
        pen.lt(3)
        pen.forward(a)
        pen.end_fill()

# 绘制左耳朵
pen.color((255, 155, 192), 'pink')
pen.penup()
pen.setheading(90)
pen.forward(-7)
pen.setheading(0)
pen.forward(70)
pen.pendown()
pen.begin_fill()
pen.setheading(100)
pen.circle(-50, 50)
pen.circle(-10, 120)
pen.circle(-50, 54)
pen.end_fill()

# 绘制右耳朵
pen.penup()
pen.setheading(90)
pen.forward(-12)
pen.setheading(0)
pen.forward(30)
pen.pendown()
pen.begin_fill()
pen.setheading(100)
pen.circle(-50, 50)
pen.circle(-10, 120)
pen.circle(-50, 56)
pen.end_fill()

# 绘制左眼睛
pen.color((255, 155, 192), 'white')
pen.penup()
pen.setheading(90)
pen.forward(-20)
pen.setheading(0)
pen.forward(-95)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# 绘制左眼珠
pen.color('black')
pen.penup()
pen.setheading(90)
pen.forward(12)
pen.setheading(0)
pen.forward(-3)
pen.pendown()
pen.begin_fill()
pen.circle(3)
pen.end_fill()

# 绘制右眼睛
pen.color((255, 155, 192), 'white')
pen.penup()
pen.setheading(90)
pen.forward(-25)
pen.setheading(0)
pen.forward(40)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# 绘制右眼珠
pen.color('black')
pen.penup()
pen.setheading(90)
pen.forward(12)
pen.setheading(0)
pen.forward(-3)
pen.pendown()
pen.begin_fill()
pen.circle(3)
pen.end_fill()

# 绘制脸蛋
pen.color((255, 155, 192))
pen.penup()
pen.setheading(90)
pen.forward(-95)
pen.setheading(0)
pen.forward(65)
pen.pendown()
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# 绘制嘴
pen.color((239, 69, 19))
pen.penup()
pen.setheading(90)
pen.forward(15)
pen.setheading(0)
pen.forward(-100)
pen.pendown()
pen.setheading(-80)
pen.circle(30, 40)
pen.circle(40, 80)

# 绘制身子，并填充上红色
pen.color('red', (255, 99, 71))
pen.penup()
pen.setheading(90)
pen.forward(-20)
pen.setheading(0)
pen.forward(-78)
pen.pendown()
pen.begin_fill()
pen.setheading(-130)
pen.circle(100, 10)
pen.circle(300, 30)
pen.setheading(0)
pen.forward(230)
pen.setheading(90)
pen.circle(300, 30)
pen.circle(100, 3)
pen.color((255, 155, 192), (255, 100, 100))
pen.setheading(-135)
pen.circle(-80, 63)
pen.circle(-150, 24)
pen.end_fill()

# 绘制左手
pen.color((255, 155, 192))
pen.penup()
pen.setheading(90)
pen.forward(-40)
pen.setheading(0)
pen.forward(-27)
pen.pendown()
pen.setheading(-160)
pen.circle(300, 15)
pen.penup()
pen.setheading(90)
pen.forward(15)
pen.setheading(0)
pen.forward(0)
pen.pendown()
pen.setheading(-10)
pen.circle(-20, 90)

# 绘制右手
pen.penup()
pen.setheading(90)
pen.forward(30)
pen.setheading(0)
pen.forward(237)
pen.pendown()
pen.setheading(-20)
pen.circle(-300, 15)
pen.penup()
pen.setheading(90)
pen.forward(20)
pen.setheading(0)
pen.forward(0)
pen.pendown()
pen.setheading(-170)
pen.circle(20, 90)

# 绘制左腿
pen.pensize(10)
pen.color((240, 128, 128))
pen.penup()
pen.setheading(90)
pen.forward(-75)
pen.setheading(0)
pen.forward(-180)
pen.pendown()
pen.setheading(-90)
pen.forward(40)
pen.setheading(-180)
pen.color('black')
pen.pensize(15)
pen.forward(20)

# 绘制右腿
pen.pensize(10)
pen.color((240, 128, 128))
pen.penup()
pen.setheading(90)
pen.forward(40)
pen.setheading(0)
pen.forward(90)
pen.pendown()
pen.setheading(-90)
pen.forward(40)
pen.setheading(-180)
pen.color('black')
pen.pensize(15)
pen.forward(20)

# 绘制尾巴
pen.pensize(4)
pen.color((255, 155, 192))
pen.penup()
pen.setheading(90)
pen.forward(70)
pen.setheading(0)
pen.forward(95)
pen.pendown()
pen.setheading(0)
pen.circle(70, 20)
pen.circle(10, 330)
pen.circle(70, 30)

turtle.done()








