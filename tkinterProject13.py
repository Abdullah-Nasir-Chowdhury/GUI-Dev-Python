# Use Radio Buttons to order pizza toppings:

# Import:
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

# Initialize GUI:
gui = Tk()
gui.title("Pizza Toppings:")
gui.iconbitmap(r".\images\favicon.ico")

# Initialize Frame:
frame = LabelFrame(gui,
                   text="Pizza Toppings!",
                   padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)


# Initialize list of Toppings:
LIST = [
    ("CHEESE", "CHEESE"),
    ("PEPPERONI", "PEPPERONI"),
    ("ONION", "ONION"),
    ("GARLIC", "GARLIC")
]

pizza = StringVar()
# pizza.set("PIZZA ")

for text, mode in LIST:
    Select = Radiobutton(frame, text=text, variable=pizza, value=mode, command=lambda: pizza.get())
    Select.grid()


def clicked(value):
    myClick = Label(frame2, text=value)
    myClick.grid()


# Initialize Button:
Enter = Button(frame, text="Enter!", command=lambda: clicked(pizza.get()))
Enter.grid(sticky=S)

frame2 = LabelFrame(gui, text="Your Choice:")
frame2.grid(row=0, column=1)
# Initialize Label:
myLabel = Label(frame2, text="You chose the topping:")

myLabel.grid()
gui.mainloop()
