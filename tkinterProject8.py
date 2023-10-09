# Using icons, images and exit buttons

# Import modules:
from tkinter import *
from PIL import Image, ImageTk

# Declare:
root = Tk()
root.title("Icons, Images and Exit")

# Create icon:
photo = ImageTk.PhotoImage(file="ytdl_icon.png")
root.wm_iconphoto(False, photo)

# exit button:
button_quit = Button(root, text="Exit", bg="Red", command=root.quit)
button_quit.grid(row=1, column=0, columnspan=5, padx=50)

# insert image:
my_img = ImageTk.PhotoImage(Image.open("ytdl_icon.png"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0)

root.mainloop()
