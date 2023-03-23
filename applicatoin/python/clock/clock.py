from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = Tk()
root.title("clock")
label = Label(root, font = ("ds-digital", 80),background = "black", foreground = "cyan")
label.pack(anchor='center')
time()
mainloop()
