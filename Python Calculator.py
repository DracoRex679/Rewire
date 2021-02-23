from tkinter import *

root = Tk()
root.title("Python Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_add(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
    return

def button_clear():
    entry.delete(0, END)
    return

def button_addition():
    first_number = entry.get()
    global first_num
    global math
    math = "addition"
    first_num = float(first_number)
    entry.delete(0, END)
    return

def button_subtract():
    first_number = entry.get()
    global first_num
    global math
    math = "subtraction"
    first_num = float(first_number)
    entry.delete(0, END)
    return

def button_multiply():
    first_number = entry.get()
    global first_num
    global math
    math ="multiplication"    
    first_num = float(first_number)
    entry.delete(0, END)
    return

def button_divide():
    first_number = entry.get()
    global first_num
    global math
    math = "division"
    first_num = float(first_number)
    entry.delete(0, END)
    return

def button_exponent():
    first_number = entry.get()
    global first_num
    global math
    math = "exponent"
    first_num = float(first_number)
    entry.delete(0, END)
    return

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, first_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, first_num - float(second_number))
    elif math == "multiplication":
         entry.insert(0, first_num * float(second_number))
    elif math == "division":
            entry.insert(0, first_num / float(second_number))
    elif math == "exponent":
            entry.insert(0, first_num ** float(second_number))

def Click():
    hello = "Hello " + entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
oneButton = Button(root, text ="1", padx=40, pady=20, command=lambda: button_add(1))
twoButton = Button(root, text ="2", padx=40, pady=20, command=lambda: button_add(2))
threeButton = Button(root, text ="3", padx=40, pady=20, command=lambda: button_add(3))
fourButton = Button(root, text ="4", padx=40, pady=20, command=lambda: button_add(4))
fiveButton = Button(root, text ="5", padx=40, pady=20, command=lambda: button_add(5))
sixButton = Button(root, text ="6", padx=40, pady=20, command=lambda: button_add(6))
sevenButton = Button(root, text ="7", padx=40, pady=20, command=lambda: button_add(7))
eightButton = Button(root, text ="8", padx=40, pady=20, command=lambda: button_add(8))
nineButton = Button(root, text ="9", padx=40, pady=20, command=lambda: button_add(9))
zeroButton = Button(root, text ="0", padx=40, pady=20, command=lambda: button_add(0))
addButton = Button(root, text ="+", padx=40, pady=20, command=lambda: button_addition())
subtractButton = Button(root, text="-", padx=40, pady=20, command=lambda: button_subtract())
multiplyButton = Button(root, text="*", padx=40, pady=20, command=lambda: button_multiply())
divisionButton = Button(root, text="/", padx=40, pady=20, command=lambda: button_divide())
clearButton = Button(root, text="clear", padx=30, pady=20, command=lambda: button_clear())
equalButton = Button(root, text="=", padx=40, pady=20, command=lambda: button_equal())
piButton = Button(root, text="pi", padx=40, pady=20, command=lambda: button_add(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679))
decimalButton = Button(root, text =".", padx=40, pady=20, command=lambda: button_add("."))
exponentButton = Button(root, text="exp", padx=40, pady=20, command=lambda: button_exponent())

oneButton.grid(row=1, column=0)
twoButton.grid(row=1, column=1)
threeButton.grid(row=1, column=2)
fourButton.grid(row=2, column=0)
fiveButton.grid(row=2, column=1)
sixButton.grid(row=2, column=2)
sevenButton.grid(row=3, column=0)
eightButton.grid(row=3, column=1)
nineButton.grid(row=3, column=2)
zeroButton.grid(row=4, column=1)
addButton.grid(row=1, column=3)
subtractButton.grid(row=2, column=3)
multiplyButton.grid(row=3, column=3)
equalButton.grid(row=4, column=2)
divisionButton.grid(row=4, column=3)
clearButton.grid(row=4, column=0)
piButton.grid(row=5, column=1)
decimalButton.grid(row=5, column=0)
exponentButton.grid(row=5, column=2)


root.mainloop()