# Create Databases:

# import modules: import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import os
import sys
import pathlib
import sqlite3

root = Tk()
root.title("Create Databases:")
root.geometry("500x500")
root.iconbitmap(r".\images\favicon.ico")

# Databases:

# Create a database or connect to one:
conn = sqlite3.connect("address_book.db")

# Create Cursor:
c = conn.cursor()

# Create Table:
c.execute("""CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text, 
        zipcode integer)""")

# Commit Changes:
conn.commit()

# Close Connections:
conn.close()

root.mainloop()

