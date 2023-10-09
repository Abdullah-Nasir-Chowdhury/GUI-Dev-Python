# input fields

from tkinter import *

root = Tk()

# entry widget:
e = Entry(root,
          width=50,
          bg="blue",
          fg="white",
          borderwidth=5)
e.pack()
# put default text inside entry box
e.insert(0, "Enter your name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter!", command=myClick)
myButton.pack()

root.mainloop()
