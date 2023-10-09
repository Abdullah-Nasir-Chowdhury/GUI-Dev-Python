# Use Radio Buttons:

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Radio Buttons")
root.iconbitmap(r".\images\favicon.ico")

# Initialize Variable:
r = IntVar()
# Set it:
# r.set("2")

def clicked(value):
    RadioClicked = Label(root, text=value)
    RadioClicked.pack()


Radiobutton(root, text="Option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option3", variable=r, value=3, command=lambda: clicked(r.get())).pack()

# Use button to take input:
myButton = Button(root, text="Enter!", command=lambda: clicked(r.get()))
myButton.pack() 

root.mainloop()
