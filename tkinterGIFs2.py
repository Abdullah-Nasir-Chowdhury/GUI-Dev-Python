
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk

window = Tk()

window.title('Grand Canyon')

canvas = Canvas(window, width=500, height=500)
canvas.pack()

my_image = PhotoImage(r"C:\Users\HP\Desktop\ytVidDownloader\images\CeEOy.gif")
canvas.create_image(0, 0, anchor=NW, image=my_image)

window.mainloop()
