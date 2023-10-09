# Order Pizza Toppings by what we have learnt so far:

# Imports:
from tkinter import *
from PIL import Image, ImageTk
import os
import sys
import tkinter

# Initialize GUI:
gui = Tk()
gui.title("Pizza Toppings Selector")
gui.iconbitmap(r".\images\favicon.ico")

# Initialize frames:
frame1 = LabelFrame(gui, text="Pizza Toppings:", padx=10, pady=10)
frame1.grid(row=0, column=0, sticky=W)

frame2 = LabelFrame(gui, text="Selected Toppings:", padx=10, pady=10)
frame2.grid(row=0, column=1, sticky=E)

# Initialize Toppings List:
Toppings = [
    ("Mushroom", "Mushroom"), ("Cheese", "Cheese"), ("Pepperoni", "Pepperoni"), ("Meat King", "Meat King")
]

# Initialize Radio Button:
pizza = StringVar()
for name, topping in Toppings:
    Radiobutton(frame1, text=name, variable=pizza, value=topping, command=lambda: pizza.get()).grid()


#     Define Button command:
def clicked(topping):
    Order_taken = Label(frame2, text=topping)
    Order_taken.grid()


# Initialize Order Button:
Order = Button(frame1, text="Enter!", bg="green", borderwidth=2, command=lambda: clicked(pizza.get()))
Order.grid(sticky=S)


gui.mainloop()
