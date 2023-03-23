import tkinter
import customtkinter
from pytube import YouTube

def start_downloud():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        print("downloud completed")
    except:
        print("youtube link is invalied")


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("youtube downlouder")

title = customtkinter.CTkLabel(app, text="insert link")
title.pack(padx=10,pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


download =customtkinter.CTkButton(app, text="Dowloud", command=start_downloud)
download.pack()
app.mainloop()
