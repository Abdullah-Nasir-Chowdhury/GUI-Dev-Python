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
var = StringVar()
drop = OptionMenu(root, var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop.pack()

root.mainloop()
