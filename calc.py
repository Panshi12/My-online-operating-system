from tkinter import*


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")


def btnequalsinput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


cal = Tk()
cal.title("calculator")
operator = ""
text_input = StringVar()

txtdisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input,
                   bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)
btn7 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="7", command=lambda: btnclick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="8", command=lambda: btnclick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="9", command=lambda: btnclick(9)).grid(row=1, column=2)
addition = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="+", command=lambda: btnclick("+")).grid(row=1, column=3)

# row 1 completed-----------------------------------------
btn4 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="4", command=lambda: btnclick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="5", command=lambda: btnclick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="6", command=lambda: btnclick(6)).grid(row=2, column=2)
subtraction = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="-", command=lambda: btnclick("-")).grid(row=2, column=3)

# row 2 completed-----------------------------------------
btn3 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="3", command=lambda: btnclick(3)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="2", command=lambda: btnclick(2)).grid(row=3, column=1)
btn1 = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="1", command=lambda: btnclick(1)).grid(row=3, column=2)
multiply = Button(cal, padx=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="*", command=lambda: btnclick("*")).grid(row=3, column=3)

# row 3 completed-----------------------------------------
btn0 = Button(cal, padx=16, pady=16,  bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="0", command=lambda: btnclick(0)).grid(row=4, column=0)
btnclear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="C", command=btncleardisplay).grid(row=4, column=1)
btnequal = Button(cal, padx=16, pady=16,  bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="=", command=btnequalsinput).grid(row=4, column=2)
divide = Button(cal, padx=16, pady=16,  bd=8, fg="black", font=(
    'arial', 20, 'bold'), text="/", command=lambda: btnclick("/")).grid(row=4, column=3)
cal.mainloop()
