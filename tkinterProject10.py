# Adding a Status Bar:
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# initialize gui:
gui = Tk()
gui.title("Image Viewer")
title = Label(gui, text="Abdullah's Image Viewer:")
title.grid(row=0, column=0, columnspan=10)

# Icon:
gui.iconbitmap(r".\images\favicon.ico")

# Create image list:
image_list = []
folder_dir = r".\images"

for images in os.listdir(folder_dir):
    if (images.endswith(".png") or
            images.endswith(".jpg") or
            images.endswith(".jpeg") or
            images.endswith(".tif") or
            images.endswith(".jfif") or
            images.endswith(".ico")):
        image_list.append(images)
        image_count = len(image_list)

# initialize images:
count = 0
image = []
while count != image_count:
    image.append(ImageTk.PhotoImage(Image.open(r".\images\\" + image_list[count])))
    count = count + 1

# initialize labels:
count = 0
label = []
while count != image_count:
    label.append(Label(image=image[count]))
    count = count + 1

# display first image:
label[0].grid(row=1, column=1)

# initialize status bar:
count = 0
status = Label(gui,
               text="Image" + str(count + 1) + "of" + str(image_count),
               bd=2,
               fg="grey",
               anchor=E,
               relief=SUNKEN
               )
status.grid(row=3,
            column=3,
            sticky=W+E)


# define button actions:
def forward():
    global count
    if count < image_count:
        label[count].grid_forget()
        count = count + 1
        if count < image_count:
            label[count].grid(row=1, column=1)
            status_update = Label(gui,
                                  text="Image" + str(count + 1) + "of" + str(image_count),
                                  fg="grey",
                                  bd=2,
                                  relief=SUNKEN,
                                  anchor=E
                                  )
            status_update.grid(row=3,
                               column=3,
                               columnspan=2,
                               sticky=W + E)
        else:
            count = 0
            label[count].grid(row=1, column=1)


def back():
    global count
    if count < image_count:
        label[count].grid_forget()
        count = count - 1
        if count >= 0:
            label[count].grid(row=1, column=1)
            status_update = Label(gui,
                                  text="Image" + str(count + 1) + "of" + str(image_count),
                                  fg="grey",
                                  bd=2,
                                  relief=SUNKEN,
                                  anchor=E)
            status_update.grid(row=3,
                               column=3,
                               sticky=W + E)  # West means left and east means right, w+e means stretch from left to right
        else:
            count = 0
            label[count].grid(row=1, column=1)


button_forward = Button(gui, text=">>", command=lambda: forward())
button_back = Button(gui, text="<<", command=back)
button_exit = Button(gui, text="Close", bg="Red", fg="white", command=gui.quit)

button_forward.grid(row=2, column=2)
button_back.grid(row=2, column=0)
button_exit.grid(row=2, column=1)

gui.mainloop()
