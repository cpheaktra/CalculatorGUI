from tkinter import *

expression = ""

def press(key):
    global expression
    expression = expression + str(key)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# About Us Page
def openAboutOnNewWindow():
    # open new window
	newWindow = Toplevel(master)
	members = ["Chhay Pheaktra", "Hea Choeurn", "Hian Yan", "Hok Kimhai",
                "Ho Vanda", "Kim Sanha", "Heng Sothib", "Dom Raksmey",
                "Eng Tokla", "Sem Sokhim", "Dim Vakhim"]
    # setting on new window
	newWindow.title("About Us")
	newWindow.geometry("400x400")
	Label(newWindow, text ="About Us", font=("Arial", 14)).pack()
	Label(newWindow, text ="Our Team Member").pack()
	for i in members:
	    Label(newWindow, text = "● "+i, anchor='nw').pack(fill='both')
# Help Page
def openHelpOnNewWindow():
    # open new window
	newWindow = Toplevel(master)
    # setting on new window
	newWindow.title("Help & Support")
	newWindow.geometry("400x400")
	Label(newWindow, text ="Help & Support").pack()

# main function
if __name__ == "__main__":
    master = Tk()

    m=Menu(master)
    m.add_command(label="About", command=openAboutOnNewWindow)
    m.add_command(label="Help", command=openHelpOnNewWindow)
    m.add_command(label="Exit", command=master.destroy)
    master.configure(menu=m)

    master.title("Calculator")
    master.geometry("252x260")
    equation = StringVar()

    expression_field = Entry(master, textvariable=equation)
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=64, pady=2)

    clearBtn = Button(master, text='Clear', fg='black', bg='#ff6961', command=clear, height=2, width=25)
    clearBtn.grid(row=1, column=0, columnspan=3, pady=2)

    divide = Button(master, text=' / ', fg='black', bg='#e8ffff', command=lambda: press("/"), height=2, width=7)
    divide.grid(row=1, column=3, pady=2)

    multiply = Button(master, text=' * ', fg='black', bg='#e8ffff', command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=2, column=3, pady=2)

    minus = Button(master, text=' - ', fg='black', bg='#e8ffff', command=lambda: press("-"), height=2, width=7)
    minus.grid(row=3, column=3, pady=2)

    plus = Button(master, text=' + ', fg='black', bg='#e8ffff', command=lambda: press("+"), height=2, width=7)
    plus.grid(row=4, column=3, pady=2)

    equal = Button(master, text=' = ', fg='black', bg='#e8ffff', command=equalpress, height=2, width=7)
    equal.grid(row=5, column=3, pady=2)

    btn1 = Button(master, text=' 1 ', fg='black', bg='#fff', command=lambda: press(1), height=2, width=7)
    btn1.grid(row=2, column=0, pady=2)

    btn2 = Button(master, text=' 2 ', fg='black', bg='#fff', command=lambda: press(2), height=2, width=7)
    btn2.grid(row=2, column=1, pady=2)

    btn3 = Button(master, text=' 3 ', fg='black', bg='#fff', command=lambda: press(3), height=2, width=7)
    btn3.grid(row=2, column=2, pady=2)

    btn4 = Button(master, text=' 4 ', fg='black', bg='#fff', command=lambda: press(4), height=2, width=7)
    btn4.grid(row=3, column=0, pady=2)
    

    btn5 = Button(master, text=' 5 ', fg='black', bg='#fff', command=lambda: press(5), height=2, width=7)
    btn5.grid(row=3, column=1, pady=2)

    btn6 = Button(master, text=' 6 ', fg='black', bg='#fff', command=lambda: press(6), height=2, width=7)
    btn6.grid(row=3, column=2, pady=2)

    btn7 = Button(master, text=' 7 ', fg='black', bg='#fff', command=lambda: press(7), height=2, width=7)
    btn7.grid(row=4, column=0, pady=2)

    btn8 = Button(master, text=' 8 ', fg='black', bg='#fff', command=lambda: press(8), height=2, width=7)
    btn8.grid(row=4, column=1, pady=2)

    btn9 = Button(master, text=' 9 ', fg='black', bg='#fff', command=lambda: press(9), height=2, width=7)
    btn9.grid(row=4, column=2, pady=2)

    btn0 = Button(master, text=' 0 ', fg='black', bg='#fff', command=lambda: press(0), height=2, width=16)
    btn0.grid(row=5, column=0,columnspan=2, pady=2)

    dot = Button(master, text='.', fg='black', bg='#fff', command=lambda: press('.'), height=2, width=7)
    dot.grid(row=5, column=2, pady=2)

#end calculator
    # start the GUI
    master.mainloop()
