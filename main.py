from tkinter import*
from turtle import*
import turtle
root=Tk(className="Learn to Draw Number")
root.geometry('1000x750')
canavas1=Canvas(root,height=500,width=500)
canavas1.grid(column=3,row=3)
draw_ui=turtle.RawTurtle(canavas1)
label1=Label(text="enter upto three digit numbers").grid(column=0,row=0)
entry1=Entry(root)
entry1.grid(column=1,row=0)
label2=Label(text="Choose the Colour:")
label2.grid(column=0,row=1)
def draw(s,j,colors):
    draw_ui.speed(1)
    draw_ui.pensize(width=8)
    draw_ui.color(colors)
    if j==1:
        post_x=-200
        post_y=-100
    elif j==2:
        post_x=-75
        post_y=-100
    else:
        post_x=50
        post_y=-100
    if s=='1':
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.pendown()
        draw_ui.fd(100)
        draw_ui.backward(50)
        draw_ui.left(90)
        draw_ui.fd(100)
        draw_ui.right(45)
        draw_ui.fd(-50)
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.left(-45)
    elif s=='2':
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.left(90)
        draw_ui.fd(100)
        draw_ui.pendown()
        draw_ui.right(30)
        for i in range(245):
            draw_ui.right(1)
            draw_ui.fd(1)
        draw_ui.goto(post_x,post_y)
        draw_ui.left(30)
        draw_ui.right(250)
        draw_ui.fd(100)    
    elif s=='3':
        print(3)
        draw_ui.penup()
        draw_ui.goto(post_x,post_y) 
        draw_ui.left(90)
        draw_ui.fd(100)
        draw_ui.right(90)
        draw_ui.fd(20)
        draw_ui.pendown()
        draw_ui.fd(65)
        draw_ui.right(135)
        draw_ui.goto(post_x+45,post_y+50)
        draw_ui.left(135)
        for i in range(250):
            draw_ui.right(1)
            draw_ui.fd(0.5)
        draw_ui.right(110)

    elif s=='4':
        print(4)
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.left(90)
        draw_ui.goto(post_x+75,post_y+100)
        draw_ui.pendown()
        draw_ui.goto(post_x+75,post_y)
        draw_ui.penup()
        draw_ui.goto(post_x+75,post_y+100)
        draw_ui.pendown()
        draw_ui.goto(post_x,post_y+50)
        draw_ui.goto(post_x+100,post_y+50)
        draw_ui.right(90)
    elif s=='5':
        print(5)
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.left(90)
        draw_ui.fd(100)
        draw_ui.right(90)
        draw_ui.pendown()
        draw_ui.fd(100)
        draw_ui.left(180)
        draw_ui.fd(100)
        draw_ui.left(90)
        draw_ui.fd(45)
        draw_ui.left(90)
        for i in range(8):
            draw_ui.rt(1)
            draw_ui.fd(10)
        for i in range(50):
            draw_ui.rt(1)
            draw_ui.fd(0.5)
        for i in range(80):
            draw_ui.rt(1)
            draw_ui.fd(1)
        for i in range(10):
            draw_ui.rt(9)
            draw_ui.fd(10)
        draw_ui.fd(10)
    elif s=='6':
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.left(90)
        draw_ui.fd(100)
        draw_ui.right(90)
        draw_ui.fd(95)
        draw_ui.right(180)
        draw_ui.pendown()
        for i in range(170):
            draw_ui.left(1)
            draw_ui.fd(1)
        for i in range(75):
            draw_ui.left(2.5)
            draw_ui.fd(1)
        for i in range(9):
            draw_ui.left(1)
            draw_ui.fd(4)
        for i in range(10):
            draw_ui.left(1)
            draw_ui.fd(1)
        draw_ui.rt(10+9+75+170)
        draw_ui.left(90)
        draw_ui.rt(25)
    elif s=='7':
        print(7)
        draw_ui.penup()
        draw_ui.goto(post_x+20,post_y+100)
        draw_ui.pendown()
        draw_ui.goto(post_x+100,post_y+100)
        draw_ui.goto(post_x+45,post_y)
    elif s=='8':
        print(8)
        draw_ui.penup()
        draw_ui.goto(post_x+50,post_y+65)
        draw_ui.pendown()
        draw_ui.goto(post_x+50,post_y+75)
        draw_ui.left(90)
        draw_ui.circle(30,180)
        draw_ui.fd(10)  
        draw_ui.goto(post_x+50,post_y+25)
        draw_ui.left(180)
        draw_ui.circle(30,-180)
        draw_ui.goto(post_x+50,post_y+65)
        draw_ui.left(90)

    elif s=='9':
        print(9)
        draw_ui.penup()
        draw_ui.goto(post_x,post_y)
        draw_ui.goto(post_x+70,post_y+70)
        draw_ui.pendown()
        draw_ui.circle(30,360+90)
        draw_ui.backward(60)
        draw_ui.circle(30,-180)
        draw_ui.left(90)
    elif s=='0':
        draw_ui.penup()
        draw_ui.goto(post_x+50,post_y+75)
        draw_ui.pendown()
        draw_ui.left(90)
        draw_ui.circle(30,180)
        draw_ui.fd(40)
        draw_ui.circle(30,180)
        draw_ui.fd(40)
        draw_ui.rt(90)
        pass
    else:
        label2=Label(root,text="enter digit number only:",bg="red")
        label2.grid(column=3,row=0)
        
def clearsrc():
    canavas1.delete("all")
def submit():
    colors  = Lb1.get(Lb1.curselection())
    s=entry1.get()
    p=list(s) 
    l=len(p)
    if l<=3:
        if l==1:
            draw(p[0],1,colors)
        else:
            j=1
            for i in p:
                draw(i,j,colors)
                j=j+1
    else:
        label2=Label(root,text="enter upto 3 digit number only:",bg="red")
        label2.grid(column=2,row=0)
    entry1.delete (first=0,last=3)
Lb1=Listbox(root)
Lb1.insert(1,"red")
Lb1.insert(2,"blue")
Lb1.insert(3,"green")
Lb1.insert(4,"orange")
Lb1.grid(column=0,row=2)
button1=Button(root,text="Submit",command=lambda:submit())
button1.grid(column=1,row=2)
clr_button=Button(root,text="Clear",command=lambda:clearsrc())
clr_button.grid(column=3,row=4)
root.mainloop()