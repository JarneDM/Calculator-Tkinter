from tkinter import *
import tkinter as tk

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""


def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""


equation_text = ""

screen = tk.Tk()

icon = tk.PhotoImage(file='calculator.png')

screen.geometry("320x350")
screen.title("Calculator")
screen.iconphoto(False, icon)
screen['bg'] = 'light grey'

equation_label = StringVar()

label = Label(screen, textvariable=equation_label, font=('consoles', 20), bg="white", width=24, height=2)
label.pack()


btnFrame = tk.Frame(screen)
btnFrame.columnconfigure(0, weight=1)
btnFrame.columnconfigure(1, weight=1)
btnFrame.columnconfigure(2, weight=1)
btnFrame['bg'] = 'light grey'


btn0 = Button(btnFrame, text="0", font=('Arial', 18), width=5, command=lambda: button_press(0))
btn0.grid(row=4, columnspan=2, sticky=tk.W+tk.E, padx=5, pady=5)

btn1 = Button(btnFrame, text="1", font=('Arial', 18), width=5, command=lambda: button_press(1))
btn1.grid(row=3, column=0, sticky=tk.W+tk.E, padx=5)

btn2 = Button(btnFrame, text="2", font=('Arial', 18), width=5, command=lambda: button_press(2))
btn2.grid(row=3, column=1, sticky=tk.W+tk.E, padx=5)

btn3 = Button(btnFrame, text="3", font=('Arial', 18), width=5, command=lambda: button_press(3))
btn3.grid(row=3, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

btn4 = Button(btnFrame, text="4", font=('Arial', 18), width=5, command=lambda: button_press(4))
btn4.grid(row=2, column=0, sticky=tk.W+tk.E, padx=5)

btn5 = Button(btnFrame, text="5", font=('Arial', 18), width=5, command=lambda: button_press(5))
btn5.grid(row=2, column=1, sticky=tk.W+tk.E, padx=5)

btn6 = Button(btnFrame, text="6", font=('Arial', 18), width=5, command=lambda: button_press(6))
btn6.grid(row=2, column=2, sticky=tk.W+tk.E, padx=5)

btn7 = Button(btnFrame, text="7", font=('Arial', 18), width=5, command=lambda: button_press(7))
btn7.grid(row=1, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

btn8 = Button(btnFrame, text="8", font=('Arial', 18), width=5, command=lambda: button_press(8))
btn8.grid(row=1, column=1, sticky=tk.W+tk.E, padx=5)

btn9 = Button(btnFrame, text="9", font=('Arial', 18), width=5, command=lambda: button_press(9))
btn9.grid(row=1, column=2, sticky=tk.W+tk.E, padx=5)

btnPlus = Button(btnFrame, text="+", font=('Arial', 18), width=5, command=lambda: button_press('+'))
btnPlus.grid(row=0, column=3, sticky=tk.W+tk.E, padx=5)

btnMin = Button(btnFrame, text="-", font=('Arial', 18), width=5, command=lambda: button_press('-'))
btnMin.grid(row=1, column=3, sticky=tk.W+tk.E, padx=5)

btnStar = Button(btnFrame, text="×", font=('Arial', 18), width=5, command=lambda: button_press('×'))
btnStar.grid(row=2, column=3, sticky=tk.W+tk.E, padx=5)

btnSlash = Button(btnFrame, text="÷", font=('Arial', 18), width=5, command=lambda: button_press('÷'))
btnSlash.grid(row=3, column=3, sticky=tk.W+tk.E, padx=5)

btnComma = Button(btnFrame, text=",", font=('Arial', 18), width=5, command=lambda: button_press(','))
btnComma.grid(row=4, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

btnEqual = Button(btnFrame, text="=", font=('Arial', 18), width=5, command=equals)
btnEqual.grid(row=4, column=3, sticky=tk.W+tk.E, padx=5, pady=5)

btnClear = Button(btnFrame, text="C", font=('Arial', 18), width=5, command=lambda: clear)
btnClear.grid(row=0, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)


btnFrame.pack()
screen.resizable(False, False)
screen.mainloop()
