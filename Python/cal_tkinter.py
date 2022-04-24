from tkinter import *


class calc:
    def __init__(self, win):
        self.lb1 = Label(win, text='First No: ', font=("Times New Roman", 10))
        self.lb2 = Label(win, text='Second No: ', font=("Times New Roman", 10))
        self.lb3 = Label(win, text='Result: ', font=("Times New Roman", 10))

        self.lb1.place(x=100, y=50)
        self.lb2.place(x=100, y=100)
        self.lb3.place(x=100, y=150)

        self.e1 = Entry(win, bd=4)
        self.e2 = Entry(win, bd=4)
        self.e3 = Entry(win, bd=4)

        self.e1.place(x=170, y=50)
        self.e2.place(x=170, y=100)
        self.e3.place(x=170, y=150)

        self.btn1 = Button(win, text="Add", bd=4)
        self.btn2 = Button(win, text="Sub", bd=4)
        self.btn3 = Button(win, text="Mul", bd=4)
        self.btn4 = Button(win, text="Div", bd=4)
        self.btn5 = Button(win, text="Mod", bd=4)

        self.btn1.place(x=100, y=200)
        self.btn2.place(x=150, y=200)
        self.btn3.place(x=200, y=200)
        self.btn4.place(x=250, y=200)
        self.btn5.place(x=300, y=200)

        self.btn1.bind('<Button-1>', self.add)
        self.btn2.bind('<Button-1>', self.sub)
        self.btn3.bind('<Button-1>', self.mul)
        self.btn4.bind('<Button-1>', self.div)
        self.btn5.bind('<Button-1>', self.mod)

    def add(self, event):
        self.e3.delete(0, 'end')
        num1 = int(self.e1.get())
        num2 = int(self.e2.get())
        result = num1 + num2
        self.e3.insert(END, str(result))

    def sub(self, event):
        self.e3.delete(0, 'end')
        num1 = int(self.e1.get())
        num2 = int(self.e2.get())
        result = num1 - num2
        self.e3.insert(END, str(result))

    def mul(self, event):
        self.e3.delete(0, 'end')
        num1 = int(self.e1.get())
        num2 = int(self.e2.get())
        result = num1*num2
        self.e3.insert(END, str(result))

    def div(self, event):
        self.e3.delete(0, 'end')
        num1 = int(self.e1.get())
        num2 = int(self.e2.get())
        result = num1/num2
        self.e3.insert(END, str(result))

    def mod(self, event):
        self.e3.delete(0, 'end')
        num1 = int(self.e1.get())
        num2 = int(self.e2.get())
        result = num1 % num2
        self.e3.insert(END, str(result))


window = Tk()
c = calc(window)
window.title("Calculator")
window.geometry("400x300+10+10")
window.mainloop()
