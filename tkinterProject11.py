# Add frames to your program:

from tkinter import *
from PIL import Image, ImageTk

# Initialize gui:
root = Tk()
root.title("Add frames to your program")
root.iconbitmap(r".\images\favicon.ico")

# Initialize frame:
frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)


# Normally put button in root, but now put button in frame:
# b = Button(frame, text="Don't click here!")
# b.pack()
# within the frame you can use pack or grid one of the two!
# but not both pack and grid
b2 = Button(frame, text="Or here!", command=root.quit)
b2.grid(row=1, column=1)

root.mainloop()

