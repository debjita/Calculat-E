# import required packages
from tkinter import *

# variable to store the user entered expression
exp=''

# Function to store the values entered by user (numbers and operators)
def press(number):
    global exp
    exp+=str(number)
    equation.set(exp)

def equalpress():
    try:
        global exp
        # eval to evaluate the expression
        total = str(eval(exp))
        equation.set(total)
        # initialize the expression variable
        expression = ""
    except:
        # display syntax error if we are unable to evaluate user expression
        equation.set("Syntax error ")
        exp= ""

# Function to clear the entered expression
def clear():
    global exp
    exp=''
    equation.set('')

# To create root window
tk=Tk()
tk.configure(background="#062422")
tk.title('Calculate-E')
tk.geometry('350x500')

# To store the values entered by the user
equation=StringVar()

# Entry Box to accept the user’s expression(input)
Text_Entry_Box=Entry(tk,textvariable=equation,width=30)
Text_Entry_Box.grid(rowspan=2,columnspan=8,ipadx=140,pady=25)

button1 = Button(tk, text=' 1 ', fg='black', bg='#C4D7B2',command=lambda: press(1), height=2, width=7)
button1.grid(row=2, column=0,padx=1,pady=15)

button2 = Button(tk, text=' 2 ',fg='black', bg='#C4D7B2',command=lambda: press(2), height=2, width=7)
button2.grid(row=2, column=1)

button3 = Button(tk, text=' 3 ', fg='black', bg='#C4D7B2',command=lambda: press(3), height=2, width=7)
button3.grid(row=2, column=2)

button4 = Button(tk, text=' 4 ', fg='black', bg='#C4D7B2',command=lambda: press(4), height=2, width=7)
button4.grid(row=3, column=0,padx=1,pady=15)

button5 = Button(tk, text=' 5 ', fg='black', bg='#C4D7B2',command=lambda: press(5), height=2, width=7)
button5.grid(row=3, column=1)

button6 = Button(tk, text=' 6 ', fg='black', bg='#C4D7B2',command=lambda: press(6), height=2, width=7)
button6.grid(row=3, column=2)

button7 = Button(tk, text=' 7 ', fg='black', bg='#C4D7B2',command=lambda: press(7), height=2, width=7)
button7.grid(row=4, column=0,padx=1,pady=15)

button8 = Button(tk, text=' 8 ', fg='black', bg='#C4D7B2',command=lambda: press(8), height=2, width=7)
button8.grid(row=4, column=1)

button9 = Button(tk, text=' 9 ', fg='black', bg='#C4D7B2',command=lambda: press(9), height=2, width=7)
button9.grid(row=4, column=2)

button0 = Button(tk, text=' 0 ', fg='black', bg='#C4D7B2',command=lambda: press(0), height=2, width=7)
button0.grid(row=5, column=0,padx=1,pady=15)

plus = Button(tk, text=' + ', fg='black', bg='#E1ECC8',command=lambda: press("+"), height=2, width=7)
plus.grid(row=2, column=3)

minus = Button(tk, text=' - ', fg='black', bg='#E1ECC8',command=lambda: press("-"), height=2, width=7)
minus.grid(row=3, column=3)

multiply = Button(tk, text=' * ', fg='black', bg='#E1ECC8',command=lambda: press("*"), height=2, width=7)
multiply.grid(row=4, column=3)

divide = Button(tk, text=' / ', fg='black', bg='#E1ECC8',command=lambda: press("/"), height=2, width=7)
divide.grid(row=5, column=3)

equal = Button(tk, text=' = ', fg='black', bg='#E1ECC8',command=equalpress, height=2, width=7)
equal.grid(row=5, column=2)

clear = Button(tk, text='Clear', fg='black', bg='#F7FFE5',command=clear, height=2, width=7)
clear.grid(row=6, column=0,padx=15,columnspan=4, sticky="we")

Decimal= Button(tk, text='.', fg='black', bg='#E1ECC8',command=lambda: press('.'), height=2, width=7)
Decimal.grid(row=5, column=1)


# Run the GUI
tk.mainloop()