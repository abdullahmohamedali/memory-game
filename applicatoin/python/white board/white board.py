from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import Tk
import tkinter as ttk


root = Tk()
root.title("white board ")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

Current_x = 0
Current_y = 0
color = 'black'
tybe = 5

def locate_xy(work):

    global Current_x, Current_y

    Current_x = work.x
    Current_y = work.y
    color = 'black'

def addline(work):

    global Current_x, Current_y

    b.create_line((Current_x, Current_y, work.x, work.y), width=tybe, fill=color)
    Current_x, Current_y = work.x, work.y
def show_color(new_color):

    global color

    color = new_color
def ear():

    global type

    type = 15
    show_color('white')
    
    di_palet

colors=Canvas(root,bg="#ffffff",width=35,height=300,bd=0)
colors.place(x=30,y=60)

Button(root, text="e",bg="#f2f3f5", command=ear).place(x=30,y=330)


b = Canvas(root,width=930,height=500, background="white",cursor="hand2" )

b.place(x=100,y=10)



def di_palet():

    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, 'Button-1',lambda x: show_color('black'))
    

    id = colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('gray'))

    id = colors.create_rectangle((10,70,30,90),fill='brown4')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('red'))

    id = colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('orange'))

    id = colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('yellow'))


    id = colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('blue'))



di_palet()

b.bind('<Button-1>', locate_xy)
b.bind('<B1-Motion>', addline)




mainloop()