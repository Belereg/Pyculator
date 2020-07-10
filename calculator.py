import os
import sys
from tkinter import *
from tkinter import font


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

resource_path('calculator.ico')
answer = None
operation = 'n'


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_add():
    global answer
    global operation
    first_number = entry.get()
    operation = '+'
    answer = float(first_number)
    entry.delete(0, END)


def button_substract():
    global answer
    global operation
    first_number = entry.get()
    operation = '-'
    answer = float(first_number)
    entry.delete(0, END)


def button_multiply():
    global answer
    global operation
    first_number = entry.get()
    operation = '*'
    answer = float(first_number)
    entry.delete(0, END)


def button_divide():
    global answer
    global operation
    first_number = entry.get()
    operation = '%'
    answer = float(first_number)
    entry.delete(0, END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if operation == '+':
        entry.insert(0, float(answer) + float(second_number))
    if operation == '-':
        entry.insert(0, float(answer) - float(second_number))
    if operation == '*':
        entry.insert(0, float(answer) * float(second_number))
    if operation == '%':
        print(float(answer), " se imparte la ", float(second_number))
        entry.insert(0, float(answer) / float(second_number))
    return


def button_clear():
    print("button_clear")

    entry.delete(0, END)


root = Tk()
root.minsize(375, 260)
root.maxsize(375, 260)
#root.iconbitmap("calculator.ico")
root.title("Pyculator")
root.configure(bg='black')
myFont = font.Font(size=15)
entry = Entry(root, width=45, borderwidth=5, bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=5)
text = Label(root, text="Pyculator, basically the best calculator out there")

button_0 = Button(root, text="0", command=lambda: button_click(0), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_1 = Button(root, text="1", command=lambda: button_click(1), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_2 = Button(root, text="2", command=lambda: button_click(2), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_3 = Button(root, text="3", command=lambda: button_click(3), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_4 = Button(root, text="4", command=lambda: button_click(4), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_5 = Button(root, text="5", command=lambda: button_click(5), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_6 = Button(root, text="6", command=lambda: button_click(6), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_7 = Button(root, text="7", command=lambda: button_click(7), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_8 = Button(root, text="8", command=lambda: button_click(8), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')
button_9 = Button(root, text="9", command=lambda: button_click(9), padx=40, pady=10, font=myFont, bd=1, bg='#FFDE8E',
                  activebackground='#FFB430')

button_add = Button(root, text="+", command=button_add, padx=19, pady=10, font=myFont, bd=1, bg='#FF8BAC',
                    activebackground='#FF306B')
button_substract = Button(root, text="−", command=button_substract, padx=19, pady=10, font=myFont, bd=1, bg='#FF8BAC',
                          activebackground='#FF306B')
button_divide = Button(root, text="÷", command=button_divide, padx=19, pady=10, font=myFont, bd=1, bg='#FF8BAC',
                       activebackground='#FF306B')
button_multiply = Button(root, text="×", command=button_multiply, padx=19, pady=10, font=myFont, bd=1, bg='#FF8BAC',
                         activebackground='#FF306B')

button_equal = Button(root, text="=", command=button_equal, padx=40, pady=10, font=myFont, bd=1, bg='#BA90FF',
                      activebackground='#7E30FF')
button_clear = Button(root, text="Clear", command=button_clear, padx=22, pady=10, font=myFont, bd=1, bg='#BA90FF',
                      activebackground='#7E30FF')
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=4)
button_substract.grid(row=2, column=4)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_divide.grid(row=3, column=4)
button_multiply.grid(row=4, column=4)
# putting the buttons on the screen

root.mainloop()
