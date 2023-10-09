# Message Boxes:

# Different popups:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import sys
from os import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")
root.iconbitmap(r".\images\favicon.ico")


def popup():
    messagebox.showinfo("Showinfo popup", "You used messagebox.showinfo")


def popup2():
    messagebox.showwarning("Showwarning popup", "You used messagebox.showwarning")


def popup3():
    messagebox.showerror("showerror popup", "You used messagebox.showerror")


def popup4():
    messagebox.askquestion("askquestion", "You used messagebox.askquestion")


def popup5():
    messagebox.askokcancel("askokcancel", "You used messagebox.askokcancel")


def popup6():
    messagebox.askyesno("askyesno", "You used messagebox.askyesno")


def popup7():
    messagebox.askretrycancel("askyesno", "You used messagebox.askyesno")


def popup8():
    messagebox.askyesnocancel("askyesnocancel", "You used messagebox.askyesno")


Button(root, text="Popup", command=popup).pack()
Button(root, text="Popup2", command=popup2).pack()
Button(root, text="Popup3", command=popup3).pack()
Button(root, text="Popup4", command=popup4).pack()
Button(root, text="Popup5", command=popup5).pack()
Button(root, text="Popup6", command=popup6).pack()
Button(root, text="Popup7", command=popup7).pack()
Button(root, text="Popup8", command=popup8).pack()

root.mainloop()
