import turtle
turtle.bgcolor("light blue")
turtle.title("Dog2")

t=turtle.Turtle()
t.speed(5)
##t.hideturtle()

t.penup()#язик
t.goto(-50,-50)
t.color("pink")
t.pendown()
t.right(90)
t.begin_fill()
t.forward(150)
t.circle(50,180)
t.right(180)
t.backward(150)
t.right(90)
t.forward(100)
t.end_fill()

t.penup()#лінія на язику
t.goto(0,-50)
t.color("#C71585")
t.pendown()
t.width(5)
t.left(90)
t.forward(150)
t.left(-5)
t.circle(17,190)
t.penup()
t.goto(-34,-200)
t.pendown()
t.left(170)
t.circle(17,190)

t.color("#DEB887")#круг верхній середній
t.penup()
t.goto(0,250)
t.pendown()
t.left(85)
t.begin_fill()
t.circle(135)
t.end_fill()

t.penup()#круг лівий нижній
t.goto(-100,90)
t.pendown()
t.begin_fill()
t.circle(130)
t.end_fill()

t.penup()#круг правий нижній
t.goto(100,90)
t.pendown()
t.begin_fill()
t.circle(130)
t.end_fill()

t.penup()#ніс
t.goto(0,-15)
t.color("black")
t.pendown()
t.begin_fill()
t.circle(44)
t.end_fill()

t.penup()#круг на носі нижній
t.goto(0,-60)
t.color("white")
t.pendown()
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()#круг на носі лівий
t.goto(-12,-40)
t.color("white")
t.pendown()
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()#круг на носі правий
t.goto(12,-40)
t.color("white")
t.pendown()
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()#око ліве чорне
t.goto(-35,20)
t.color("black")
t.pendown()
def draw(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)
t.seth(45)
t.begin_fill()
draw(48)
t.end_fill()

t.penup()#око праве чорне
t.goto(65,20)
t.color("black")
t.pendown()
def draw(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)
t.seth(45)
t.begin_fill()
draw(48)
t.end_fill()

t.penup()#круг білий на лівому оці
t.goto(-40,30)
t.color("white")
t.pendown()
def draw1(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)
t.seth(45)
t.begin_fill()
draw1(27)
t.end_fill()

t.penup()#круг білий на правому оці
t.goto(55,30)
t.color("white")
t.pendown()
def draw1(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)
t.seth(45)
t.begin_fill()
draw1(27)
t.end_fill()

t.penup()
t.goto(-25,50)#коса лінія на оці лівому
t.color("black")
t.pendown()
t.right(90)
t.width(5)
t.left(360)
t.circle(100,-20)

t.penup()
t.goto(70,50)#коса лінія на правому оці
t.color("black")
t.pendown()
t.width(5)
t.left(380)
t.circle(100,-20)

t.penup()
t.goto(-87,180)#вухо ліве
t.color("#8B4513")
t.pendown()
t.right(55)
t.begin_fill()
t.width(10)
t.forward(200)
t.right(61)
t.forward(50)
t.left(125)
t.circle(120,-150)
t.end_fill()

t.penup()
t.goto(87,180)#вухо праве
t.color("#8B4513")
t.pendown()
t.left(145)
t.begin_fill()
t.width(10)
t.forward(200)
t.left(61)
t.forward(50)
t.right(305)
t.circle(120,150)
t.end_fill()

t.hideturtle()





print("end")


