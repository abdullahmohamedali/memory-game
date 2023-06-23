from tkinter import *

def left(x):
    x = -10
    y = 0
    c.move(rec, x, y)

def right(x):
    x = 10
    y = 0
    c.move(rec, x, y)
    
def up(x):
    x = 0
    y = -10
    c.move(rec, x, y)
    
def down(x):
    x = 0
    y = 10
    c.move(rec, x, y)


window = Tk()
window.title("arrow input")
window.geometry("600x500")


c = Canvas(window, width = 600, height = 500, bg = 'blue')
c.pack()

rec = c.create_rectangle(20,20,40,40, fill = "red", outline = "black")


window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

window.mainloop()