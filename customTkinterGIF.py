import os, tkinter as tk
import time
from PIL import Image as PIM, ImageTk, ImageWin
from tkinter import *
import customtkinter
from customtkinter import *


root = customtkinter.CTk()
root.title("SCP-079")
root.iconbitmap(r"C:\Users\HP\Desktop\ytVidDownloader\images\hitmanInsignia1.ico")
root.geometry("540x360")

im = PIM.open(r"C:\Users\HP\Desktop\ytVidDownloader\images\jump.gif")
frames_number = im.n_frames
CTk_image = customtkinter.CTkImage(PIM.open(r"C:\Users\HP\Desktop\ytVidDownloader\images\jump.gif"))
output = "".join("Number of frames: " + str(frames_number))
print(output)
# ph = ImageTk.PhotoImage(CTk_image)
gif = customtkinter.CTkLabel(root, image=CTk_image)
gif.image = gif

frames = [PhotoImage(file=r"C:\Users\HP\Desktop\ytVidDownloader\images\jump.gif",
                     format='gif -index %i' % i) for i in range(frames_number)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind > frames_number - 1:
        ind = 0
    gif.configure(image=frame)
    root.after(50, update, ind)


gif = customtkinter.CTkLabel(root, text="Downloaded! Weeyy!", text_color="black", font=("", 24))
gif.pack()
root.after(0, update, 0)


root.mainloop()
