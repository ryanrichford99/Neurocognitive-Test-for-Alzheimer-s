from tkinter import *


root = Tk()
root.geometry("600x800")
root.title("HOMEPAGE")
myLabel = Label(root, text="Database Input", width = 50, height = 8, fg = "red")
myLabel.pack()
speed = 0

e = Entry(root, width=50)
e.pack()

def click():
    speed = "speed Battery score saved as:" + e.get()
    mylable = Label(root,text=speed)
    mylable.pack()

mybuttonspeed = Button(root, text="Enter speed Battery Score:", command=click)
mybuttonspeed.pack()

braek1 = Label(root, text=" ")
braek1.pack()

a = Entry(root, width=50)
a.pack()

def click1():
    speed = "Accuracy Battery score saved as:" + a.get()
    mylable1 = Label(root,text=speed)
    mylable1.pack()

mybuttonacc = Button(root, text="Enter Accuracy Battery Score:", command=click1)
mybuttonacc.pack()

braek2 = Label(root, text=" ")
braek2.pack()

b = Entry(root, width=50)
b.pack()

def click2():
    speed = "Memory Battery score saved as:" + b.get()
    mylable1 = Label(root,text=speed)
    mylable1.pack()

mybuttonmem = Button(root, text="Enter Memory Battery Score:", command=click2)
mybuttonmem.pack()








root.mainloop()

