from turtle import*

def nose(x,y):#鼻子
    pu()
    goto(x,y)
    pd()
    seth(-30)
    begin_fill()
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()

    pu()
    seth(90)
    fd(25)
    seth(0)
    fd(10)
    pd()
    pencolor(255,155,192)
    seth(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

    pu()
    seth(0)
    fd(20)
    pd()
    pencolor(255,155,192)
    seth(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()


def head(x,y):#头
    color((255,155,192),"pink")
    pu()
    goto(x,y)
    seth(0)
    pd()
    begin_fill()
    seth(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    seth(161)
    circle(-300,15)
    pu()
    goto(-100,100)
    pd()
    seth(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y): #耳朵
    color((255,155,192),"pink")
    pu()
    goto(x,y)
    pd()
    begin_fill()
    seth(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()

    pu()
    seth(90)
    fd(-12)
    seth(0)
    fd(30)
    pd()
    begin_fill()
    seth(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()


def eyes(x,y):#眼睛
    color((255,155,192),"white")
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)
    pd()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()

    color((255,155,192),"white")
    pu()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)
    pd()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):#腮
    color((255,155,192))
    pu()
    goto(x,y)
    pd()
    seth(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y): #嘴
    color(239,69,19)
    pu()
    goto(x,y)
    pd()
    seth(-80)
    circle(30,40)
    circle(40,80)


def body(x,y):#身体
    color("red",(255,99,71))
    pu()
    goto(x,y)
    pd()
    begin_fill()
    seth(-130)
    circle(100,10)
    circle(300,30)
    seth(0)
    fd(230)
    seth(90)
    circle(300,30)
    circle(100,3)
    color((255,155,192),(255,100,100))
    seth(-135)
    circle(-80,63)
    circle(-150,24)
    end_fill()


def hands(x,y):#手
    color((255,155,192))
    pu()
    goto(x,y)
    pd()
    seth(-160)
    circle(300,15)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(0)
    pd()
    seth(-10)
    circle(-20,90)

    pu()
    seth(90)
    fd(30)
    seth(0)
    fd(237)
    pd()
    seth(-20)
    circle(-300,15)
    pu()
    seth(90)
    fd(20)
    seth(0)
    fd(0)
    pd()
    seth(-170)
    circle(20,90)

def foot(x,y):#脚
    pensize(10)
    color((240,128,128))
    pu()
    goto(x,y)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)

    pensize(10)
    color((240,128,128))
    pu()
    seth(90)
    fd(40)
    seth(0)
    fd(90)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)

def tail(x,y):#尾巴
    pensize(4)
    color((255,155,192))
    pu()
    goto(x,y)
    pd()
    seth(0)
    circle(70,20)
    circle(10,330)
    circle(70,30)

def setting():          #参数设置
    pensize(4)
    hideturtle()
    colormode(255)
    color((255,155,192),"pink")
    setup(840,500)
    speed(10)

def main():
    setting()           #画布、画笔设置
    nose(-100,100)      #鼻子
    head(-69,167)       #头
    ears(0,160)         #耳朵
    eyes(0,140)         #眼睛
    cheek(80,10)        #腮
    mouth(-20,30)       #嘴
    body(-32,-8)        #身体
    hands(-56,-45)      #手
    foot(2,-177)        #脚
    tail(148,-155)      #尾巴
    done()              #结束

main()