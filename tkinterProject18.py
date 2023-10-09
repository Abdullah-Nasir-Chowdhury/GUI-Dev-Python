# Checkboxes:

# import modules:
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys

root = Tk()
root.title("Checkboxes")
root.geometry("500x500")
root.iconbitmap(r".\images\favicon.ico")

# Create tkinter variable:
# Create Integer Variable:
var_integer = IntVar()
# Create String Variable:
var_string = StringVar()

c = Checkbutton(root, text="Check this box.", variable=var_integer)
c.pack()
c_advanced = Checkbutton(root, text="Advanced Check Box", variable=var_string, onvalue="on", offvalue="off")
c_advanced.deselect()
c_advanced.pack()


def show():
    my_label = Label(root, text=var_integer.get())
    my_label.pack()
    my_label2 = Label(root, text=var_string.get())
    my_label2.pack()


myButton = Button(root, text="Enter", command=show)
myButton.pack()

root.mainloop()
