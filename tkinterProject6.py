from tkinter import *

f_num = ""
math = ""

root = Tk()
root.title("Simple Calculator")

Title = Label(root, text="Abdullah's Calculator")
Title.grid(row=0, column=0, columnspan=6)

e = Entry(root, width="50", borderwidth="5")
e.grid(row=1, column=1, columnspan=6, padx="10", pady="10")


# Define Button Command:
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))


# Define Buttons
Button_1 = Button(root, text="1", padx="40", pady="40", command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx="40", pady="40", command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx="40", pady="40", command=lambda: button_click(3))

Button_4 = Button(root, text="4", padx="40", pady="40", command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx="40", pady="40", command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx="40", pady="40", command=lambda: button_click(6))

Button_7 = Button(root, text="7", padx="40", pady="40", command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx="40", pady="40", command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx="40", pady="40", command=lambda: button_click(9))

Button_0 = Button(root, text="0", padx="40", pady="40", command=lambda: button_click(0))

Button_clear = Button(root, text="AC", padx="40", pady="40", command=button_clear)
Button_add = Button(root, text="+", padx="40", pady="40", command=button_add)
Button_equal = Button(root, text="=", padx="40", pady="40", command=button_equal)
Button_sub = Button(root, text="-", padx="40", pady="40", command=button_sub)
Button_mult = Button(root, text="*", padx="40", pady="40", command=button_mult)
Button_div = Button(root, text="/", padx="40", pady="40", command=button_div)


# Put the button on screen:
Button_1.grid(row=3, column=1)
Button_2.grid(row=3, column=2)
Button_3.grid(row=3, column=3)

Button_4.grid(row=4, column=1)
Button_5.grid(row=4, column=2)
Button_6.grid(row=4, column=3)

Button_7.grid(row=5, column=1)
Button_8.grid(row=5, column=2)
Button_9.grid(row=5, column=3)

Button_0.grid(row=6, column=2)
Button_add.grid(row=6, column=1)
Button_equal.grid(row=6, column=3)

Button_sub.grid(row=6, column=4)
Button_mult.grid(row=5, column=4)
Button_div.grid(row=4, column=4)

Button_clear.grid(row=7, column=0, columnspan=4)

root.mainloop()
