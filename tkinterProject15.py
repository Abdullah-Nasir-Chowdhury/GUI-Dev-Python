# Create Windows:

# Import modules:
import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sys
import pathlib
import PIL
from PIL import Image, ImageTk


# define GUI:
gui = Tk()
gui.title("Create Windows")
gui.iconbitmap(r".\images\favicon.ico")

# define new window by Toplevel() function:
top = Toplevel()
top.title("Second Window")
top.iconbitmap(r".\images\favicon.ico")
my_img = ImageTk.PhotoImage(Image.open(r".\images\favicon.ico"))
my_label = Label(top, image=my_img)
my_label.pack()

gui.mainloop()



