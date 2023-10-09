# Create Sliders:

# import module:
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Sliders")
root.iconbitmap(r".\images\favicon.ico")
# Create 500x500 window:
root.geometry("500x500")


my_label = Label(root, text=" Vertical Slider")
my_label.pack()
vertical = Scale(root, from_=0, to=500)
vertical.pack()

my_label2 = Label(root, text=" Horizontal Slider")
my_label.pack()
horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)
horizontal.pack()

my_label3 = Label(root, text=horizontal.get())
my_label3.pack()


def slide():
    my_label4 = Label(root, text=horizontal.get())
    my_label4.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


my_btn = Button(root, text="Click Me!", command=slide)
my_btn.pack()


root.mainloop()
