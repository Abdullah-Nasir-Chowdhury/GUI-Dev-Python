# Database Creation Project:

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

# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)""")

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Labels:
f_name_label = Label(root, text="First Name:")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name:")
l_name_label.grid(row=1, column=0)
address = Label(root, text="Address:")
address.grid(row=2, column=0)
city = Label(root, text="City:")
city.grid(row=3, column=0)
state = Label(root, text="State:")
state.grid(row=4, column=0)
zipcode = Label(root, text="zipcode:")
zipcode.grid(row=5, column=0)


# Create Submit Button:
def submit():
    # Create a database or connect to one:
    conn = sqlite3.connect("address_book.db")

    # Create Cursor:
    c = conn.cursor()

    # Insert into Table:
    c.execute("INSERT INTO" addresses "VALUES" (':f_name', ':last_name', ':address', ':city', ':state', ':zipcode'),
              {
                  'f_name': f_name.get(),
                  'last_name': last_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              }
              )

    # Commit Changes:
    conn.commit()

    # Close Connection:
    conn.close()

    # Clear the text Boxes
    f_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


submit_btn = Button(root, text="Add Record to Database!", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# Commit Changes:
conn.commit()

# Close Connections:
conn.close()

root.mainloop()
