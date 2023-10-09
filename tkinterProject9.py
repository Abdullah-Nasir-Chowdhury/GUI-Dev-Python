# Build an image viewer app

from tkinter import *
from PIL import Image, ImageTk
import os

# initialize gui:
root = Tk()
root.title("Image Viewer")
title = Label(root, text="Image Viewer:")
title.grid(row=0, column=0, columnspan=4)

# Create Icon
photo = ImageTk.PhotoImage(file=r".\images\favicon.ico")
root.iconbitmap(r".\images\favicon.ico")

# Count:
image_count = []

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

# my_label = []
# print(my_label)
# print(image_list[1])
# print("images\\"+image_list[1])

# test:
# img1 = ImageTk.PhotoImage(Image.open(r".\images\\" + image_list[1]))
# my_labeel = Label(image=img1)
# my_labeel.pack()

# initialize images:
count = 0
my_image = []
while count != image_count:
    my_image.append(ImageTk.PhotoImage(Image.open(r".\images\\" + image_list[count])))
    count = count + 1
# initialize labels:
count = 0
my_label = []
while count != image_count:
    my_label.append(Label(image=my_image[count]))
    # my_label[count].grid(row=0, column=count, columnspan=2)
    count = count + 1

my_label[0].grid(row=1, column=0, columnspan=3)

# define button actions:
count = 0


def forward():
    global count
    my_label[count].grid_forget()
    count = count + 1
    if count >= image_count:
        count = 0
    my_label[count].grid(row=1, column=0, columnspan=3)


def back():
    global count
    my_label[count].grid_forget()
    count = count-1
    if count < 0:
        count = 0
    my_label[count].grid(row=1, column=0, columnspan=3)


# initialize buttons:
button_back = Button(root, text="<<", command=back)
button_forward = Button(root, text=">>", command=lambda: forward())
button_exit = Button(root, text="Close", bg="Red", fg="White", command=root.quit)
# position buttons:
button_back.grid(row=2, column=0)
button_forward.grid(row=2, column=2)
button_exit.grid(row=2, column=1)

root.mainloop()
