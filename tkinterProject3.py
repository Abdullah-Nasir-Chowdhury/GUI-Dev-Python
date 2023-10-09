# Buttons!

from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()


def myClick2():
    myLabel2 = Label(root, text="Look! You clicked Red Text Button!")
    myLabel2.pack()


def myClick3():
    myLabel3 = Label(root, text="Look!I am Red~")
    myLabel3.pack()
    

# Disable button:
myButton = Button(root, text=" Don't Click Me!", state=DISABLED)
myButton.pack()
# Don't Disable it:
myButton1 = Button(root, text="Click Me!")
myButton1.pack()
# Increase Button size:
# length
myButton2 = Button(root, text="Longer!", padx="50")
myButton2.pack()
# width
myButton3 = Button(root, text="Taller!", pady="50")
myButton3.pack()
# Bigger!
myButton4 = Button(root, text="Bigger!", padx="50", pady="50")
myButton4.pack()
# Look I clicked a Button!!
myButton5 = Button(root, text="Click a Button!", command=myClick)
myButton5.pack()
# Look I am red!!
myButton6 = Button(root, text="Click Red Button!", command=myClick2, fg="red")
myButton6.pack()
# Look RedBackGround!
myButton7 = Button(root, text="Click RedBackGround Button", command=myClick3, bg="red")
myButton7.pack()

root.mainloop()
