# Open Files Dialogue Box

# Import modules:
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import os
import sys
import pathlib

# Initialize GUI:
GUI = Tk()
GUI.title("Open Files Dialog Box")
GUI.iconbitmap(r".\images\favicon.ico")

# Provide path to directory:
initial_dir = r".\images"

# Initialize Open files Dialogue Box
GUI.filename = filedialog.askopenfilename(initialdir=initial_dir,
                                          title="Select a file",
                                          filetypes=(("PNG files", "*.png"),
                                                     ("All files", "*.*")))

# See what the above definition returns:
my_label = Label(GUI, text=GUI.filename)
my_label.pack()

# Use the GUI.filename function to open image or any other thing:
my_image = ImageTk.PhotoImage(Image.open(GUI.filename))
my_image_label = Label(GUI, image=my_image)
my_image_label.pack()

GUI.mainloop()


