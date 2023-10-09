# Create message box interface:

# press ctrl + . to hide import at the end of imported modules:
# import dependencies:
import tkinter
import os
import sys
import PIL
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# Initialize GUI:
gui = Tk()
gui.title("Message boxes")
gui.iconbitmap(r".\images\favicon.ico")


def popup():
    response = messagebox.askquestion("AskQuestion", "Yes or No?")
    Label(gui, text=response).pack()
    if response == "yes":
        Label(gui, text="You clicked Yes").pack()
    else:
        Label(gui, text="You clicked No").pack()


AskQuestion = Button(gui, text="AskQuestion", command=popup)
AskQuestion.pack()

gui.mainloop()
