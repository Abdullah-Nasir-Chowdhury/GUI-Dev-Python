# Call other windows from original window:

# Import modules:
import tkinter
from tkinter import *
from tkinter import messagebox
import PIL
import os
import pathlib
import sys
from PIL import Image, ImageTk

# Initialize root gui:
RootGUI = Tk()
RootGUI.title("Main window")
RootGUI.iconbitmap(r".\images\favicon.ico")

# Initialize image to be displayed:
my_img = ImageTk.PhotoImage(Image.open(r".\images\favicon.ico"))


# Define open button:
def open():
    top = Toplevel()
    top.title("New Window")
    top.iconbitmap(r".\images\favicon.ico")
    my_label = Label(top, image=my_img)
    my_label.pack()


# Initialize Button:
btn = Button(RootGUI, text="Open second window", command=open)
btn.pack()


RootGUI.mainloop()