#!/usr/bin/env python3

from calculator import calculator
from tkinter import *

root = Tk()
root.title("Python calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current+str(number))

def button_clear():
    e.delete(0, END)

def button_calculate(string):
    operation = calculator(string)
    e.delete(0, END)
    e.insert(0, operation.result)
    print(operation.result)

_padx = 40
_pady = 20

#Define buttons

button_1 = Button(root, text="1", padx=_padx, pady=_pady, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=_padx, pady=_pady, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=_padx, pady=_pady, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=_padx, pady=_pady, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=_padx, pady=_pady, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=_padx, pady=_pady, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=_padx, pady=_pady, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=_padx, pady=_pady, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=_padx, pady=_pady, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=_padx, pady=_pady, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=_padx, pady=_pady, command=lambda: button_click('+'))
button_minus = Button(root, text="-", padx=_padx, pady=_pady, command=lambda: button_click('-'))
button_multiply = Button(root, text="*", padx=_padx, pady=_pady, command=lambda: button_click('*'))
button_divide = Button(root, text="/", padx=_padx, pady=_pady, command=lambda: button_click('/'))
button_modulo = Button(root, text="%", padx=_padx, pady=_pady, command=lambda: button_click('%'))
button_exp = Button(root, text="e", padx=_padx, pady=_pady, command=lambda: button_click('e'))

button_equal = Button(root, text="=", padx=_padx, pady=_pady, command=lambda: button_calculate(e.get()))
button_clear = Button(root, text="C", padx=_padx, pady=_pady, command=lambda: button_clear())

#Display buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_modulo.grid(row=5, column=3)

root.mainloop()

# test = calculator('1+3*2^2-5')
# print(test.result)