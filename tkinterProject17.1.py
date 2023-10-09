# Create a difficulty slider:

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys
import pathlib

root = Tk()
root.title("Difficulty Slider")
root.iconbitmap(r".\images\favicon.ico")
root.geometry("500x500")


class Difficulty:

    def __init__(self, master):
        self.vel_1 = IntVar()
        self.levels = ['Insane', 'Hard', 'Challenging', 'Normal', 'Easy', 'Walk in the Park', 'Story Mode']
        self.dif_scale = Scale(master, variable=self.vel_1, from_=3, to=-3, resolution=1, orient=HORIZONTAL, length=450,
                               tickinterval=1, label="Your Dice Roll Modifier", showvalue=0, command=self.Adjust_scl)
        self.dif_scale.pack()

        self.dif_label = Label(master)
        self.dif_label.pack()

    def Adjust_scl(self, random_parameter):
        level = self.vel_1.get() + 3
        print(level)
        self.dif_label.config(text=self.levels[level])


dif = Difficulty(root)

root.mainloop()