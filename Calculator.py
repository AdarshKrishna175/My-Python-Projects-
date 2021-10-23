# import everthing from tkinter module
from tkinter import *  # import from
import random  # importto


# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # try and exept statments is used
    # for handling the errors like zero
    # division error etc

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the exept block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents


# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.geometry("225x320")
    root.title("Calculator")
    root.configure(background="black")
    equation = StringVar()
    expression_field = Entry(root, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table lik structure .
    expression_field.grid(columnspan=8, ipadx=33, ipady=10, padx=15, pady=5)
    equation.set('Enter your expression')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed
    lbl1= Label(root, bg='black', height=3, width=1)
    lbl1.grid(row=2, column=0)
    button1 = Button(root, text=' 7 ', fg='black', bg='grey',
                    command=lambda: press(7), height=3, width=5)
    button1.grid(row=2, column=1)

    button2 = Button(root, text=' 8 ', fg='black', bg='grey',
                     command=lambda: press(8), height=3,width=5)
    button2.grid(row=2, column=2)

    button3 = Button(root, text=' 9 ', fg='black', bg='grey',
                     command=lambda: press(9), height=3,width=5)
    button3.grid(row=2, column=3)

    button4 = Button(root, text=' 4 ', fg='black', bg='grey',
                     command=lambda: press(4), height=3, width=5)
    button4.grid(row=3, column=1)

    button5 = Button(root, text=' 5 ', fg='black', bg='grey',
                     command=lambda: press(5), height=3,width=5)
    button5.grid(row=3, column=2)

    button6 = Button(root, text=' 6 ', fg='black', bg='grey',
                     command=lambda: press(6), height=3, width=5)
    button6.grid(row=3, column=3)

    button7 = Button(root, text=' 1 ', fg='black', bg='grey',
                     command=lambda: press(1), height=3, width=5)
    button7.grid(row=4, column=1)

    button8 = Button(root, text=' 2 ', fg='black', bg='grey',
                     command=lambda: press(2),height=3, width=5)
    button8.grid(row=4, column=2)

    button9 = Button(root, text=' 3 ', fg='black', bg='grey',
                     command=lambda: press(3), height=3, width=5)
    button9.grid(row=4, column=3)

    button0 = Button(root, text=' 0 ', fg='black', bg='grey',
                     command=lambda: press(0), height=3,width=5)
    button0.grid(row=5, column=1)



    plus = Button(root, text=' + ', fg='black', bg='orange',
                  command=lambda: press(' + '), height=3, width=4)
    plus.grid(row=2, column=4)

    minus = Button(root, text=' - ', fg='black', bg='orange',
                  command=lambda: press(' - '), height=3, width=4)
    minus.grid(row=3, column=4)

    multiply = Button(root, text=' * ', fg='black', bg='orange',
                  command=lambda: press(' * '), height=3, width=4)
    multiply.grid(row=4, column=4)

    divide = Button(root, text=' / ', fg='black', bg='orange',
                  command=lambda: press(' / '), height=3, width=4)
    divide.grid(row=5, column=4)

    clear = Button(root, text='Clear', fg='black', bg='grey',
                  command=clear, height=3, width=5)
    clear.grid(row=5, column=3)

    decimal = Button(root, text=' . ', fg='black', bg='grey',
                  command=lambda: press(' . '), height=3, width=5)
    decimal.grid(row=5, column=2)

    equal = Button(root, text=' = ', fg='black', bg='dark grey',
                   command=equalpress, height=2, width=25)
    equal.grid(row=6, columnspan=30)

root.mainloop()




