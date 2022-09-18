from tkinter import *

# Global variables to hold current value and operation to perform.
global current
global operation


def clear_all():
    """Clear entry widget and global variables."""
    global current
    global operation
    entry.delete(0, END)
    current = 0
    operation = ""


def clear_entry():
    """Clear current entry but leave global variables unchanged."""
    entry.delete(0, END)


def enter_num(num):
    """Add number to entry box when button pressed."""
    entry.insert(END, num)


def enter_decimal(dec, cur):
    """If no decimal in entry, add decimal, else do not add."""
    if dec not in cur:
        entry.insert(END, dec)


def neg_pos(neg, cur):
    """If positive, make negative, else if negative, make positive."""
    if neg not in cur:
        entry.insert(0, neg)
    else:
        entry.delete(0, 1)


def addition(num):
    """Save current entry and declare operation to be done as addition."""
    global current
    global operation
    current = float(num)
    operation = "add"

    entry.delete(0, END)


def subtraction(num):
    """Save current entry and declare operation to be done as subtraction."""
    global current
    global operation
    current = float(num)
    operation = "subtract"

    entry.delete(0, END)


def multiplication(num):
    """Save current entry and declare operation as multiplication."""
    global current
    global operation
    current = float(num)
    operation = "multiply"

    entry.delete(0, END)


def division(num):
    """Save current entry and declare operation to be done as division."""
    global current
    global operation
    current = float(num)
    operation = "divide"

    entry.delete(0, END)


def calculate(num):
    """Calculate equation entered using current entry and global variables."""
    global current
    global operation

    if operation == "add":
        current += float(num)
    elif operation == "subtract":
        current -= float(num)
    elif operation == "multiply":
        current *= float(num)
    elif operation == "divide":
        current /= float(num)

    entry.delete(0, END)

    # Drop the decimals if not needed and display calculated answer.
    if int(current) == current:
        entry.insert(0, str(int(current)))
    else:
        entry.insert(0, current)


# Setup root.
root = Tk()
root.title("Calculator")
root.iconbitmap("vector-calculator-icon.ico")
root.resizable(False, False)

# Create and display entry box.
entry = Entry(root, borderwidth=5, font=("helvetica", 18))
entry.grid(row=0, column=0, columnspan=5, sticky=EW)

# Create buttons.
button_0 = Button(text="0", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(0))
button_1 = Button(text="1", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(1))
button_2 = Button(text="2", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(2))
button_3 = Button(text="3", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(3))
button_4 = Button(text="4", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(4))
button_5 = Button(text="5", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(5))
button_6 = Button(text="6", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(6))
button_7 = Button(text="7", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(7))
button_8 = Button(text="8", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(8))
button_9 = Button(text="9", font=("helvetica", 12), width=5, height=2,
                  command=lambda: enter_num(9))
button_decimal = Button(text=".", font=("helvetica", 12), width=5, height=2,
                        command=lambda: enter_decimal(".", entry.get()))
button_neg = Button(text="+/-", font=("helvetica", 12), width=5, height=2,
                    command=lambda: neg_pos("-", entry.get()))
button_add = Button(text="+", font=("helvetica", 12), width=5, height=2,
                    command=lambda: addition(entry.get()))
button_minus = Button(text="-", font=("helvetica", 12), width=5, height=2,
                      command=lambda: subtraction(entry.get()))
button_multiply = Button(text="*", font=("helvetica", 12), width=5, height=2,
                         command=lambda: multiplication(entry.get()))
button_divide = Button(text="/", font=("helvetica", 12), width=5, height=2,
                       command=lambda: division(entry.get()))
button_equal = Button(text="=", font=("helvetica", 12), width=5, bg="blue",
                      fg="white", command=lambda: calculate(entry.get()))
button_clear_all = Button(text="C", font=("helvetica", 12), width=5, height=2,
                          bg="red", fg="white", command=clear_all)
button_clear_entry = Button(text="CE", font=("helvetica", 12),
                            width=5, height=2, command=clear_entry)

# Layout and display buttons.
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_minus.grid(row=1, column=3)
button_divide.grid(row=1, column=4)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_add.grid(row=2, column=3)
button_multiply.grid(row=2, column=4)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_equal.grid(row=3, column=3, rowspan=2, sticky=NS)
button_clear_entry.grid(row=3, column=4)
button_neg.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_decimal.grid(row=4, column=2)
button_clear_all.grid(row=4, column=4)

root.mainloop()
