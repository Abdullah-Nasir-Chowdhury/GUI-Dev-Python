import tkinter
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")


def button_function():
    print("button pressed")


label = customtkinter.CTkLabel(master=app, text="CTkLabel")
label.grid(row=0, column=1)

button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
