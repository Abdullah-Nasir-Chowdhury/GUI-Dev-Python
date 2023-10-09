from tkinter import *

root = Tk()

myLabel2 = Label(root, text="Please enter your name in the box below:")
myLabel2.pack()

e = Entry(root, width="50", borderwidth="3")
e.pack()


def myClick():
    hello = "hello daddy! \n" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Click!", command=myClick)
myButton.pack()

root.mainloop()
