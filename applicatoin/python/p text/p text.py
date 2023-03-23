import pyfiglet
import sqlite3
import random
import termcolor
from rich import pretty
from rich import inspect
from rich.progress import track
from time import sleep

msg = input("what would you like to print? ")
fonts = ["isometric1", "isometric3", "bell", "big",
         "block",  "alphabet"]
color = input("what is the color? ")


print(termcolor.colored(pyfiglet.figlet_format(
    msg, font=random.choice(fonts)), color=color))

status = input("whrite any thing to show status? ")
print("word: " + msg)
print("color: " + color)
print("font: " + random.choice(fonts))

close = input("press anything if you want to close? ")
print("colecting data...")
for step in track(range(30)):
    sleep(1)
    step
db = sqlite3.connect("font.db")
cr = db.cursor()
ra = random.choice(fonts)
cr.execute(
    f"insert into font  (font,color,name) values('{ra}', '{color}', '{msg}')")
print("installing...")
for step in track(range(30)):
    sleep(1)
    step

inspect('done')

db.commit()
db.close()
