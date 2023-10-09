# Dropdown boxes

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import sys
import os
import pathlib

root = Tk()
root.title("Dropdown Boxes")
root.geometry("500x500")
root.iconbitmap(r".\images\favicon.ico")

# Dropdown boxes:
# Create List:
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

var = StringVar()
var.set(options[0])
drop = OptionMenu(root, var, *options)
drop.pack()


def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()


myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

root.mainloop()
