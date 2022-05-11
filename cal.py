#A GUI Calulator using Tkinter.

#import tknker library
from tkinter import *

#Creating an object of tkinter
root = Tk()
root.title("GUI Calculator")

# function for inserting the numbers
def btn_insert(numbers):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(numbers))

#function for providing the operators
def btn_math(maths):
    global f_num
    f_num = e.get()
    e.delete(0, END)
    global oper
    oper = maths

#function to calculate the answer
def btn_equals():
    sec_num = e.get()
    e.delete(0, END)

    if oper == "+":
        e.insert(0, int(f_num) + int(sec_num))
    if oper == "-":
        e.insert(0, int(f_num) - int(sec_num))
    if oper == "*":
        e.insert(0, int(f_num) * int(sec_num))
    if oper == "/":
        e.insert(0, float(f_num) / float(sec_num))

#function to clear the textfield
def btn_clear():
    e.delete(0, END)

#Creating TextBox for Inputing
e = Entry(root, width=35, borderwidth=5)

#Creating Buttons for Numpad
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_insert(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_insert(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_insert(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_insert(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_insert(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_insert(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_insert(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_insert(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_insert(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_insert(0))

#create Buttons for choosing Operator
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: btn_math("+"))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: btn_math("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: btn_math("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: btn_math("/"))

#creating the clear and equals buttons
button_equals = Button(root, text="=", padx=40, pady=20, command=btn_equals)
button_clear = Button(root, text="CE", padx=35, pady=20, command=btn_clear)

#inserting the entry
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Insert the numpad Buttons to the GUI
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)

#insert the operator buttons to GUI
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

#inserting the extra buttons
button_clear.grid(row=4, column=0)
button_equals.grid(row=4, column=2)

root.mainloop()