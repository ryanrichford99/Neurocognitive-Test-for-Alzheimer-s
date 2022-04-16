import pygame


from tkinter import *

root = Tk()
root.geometry("600x800")
root.title("HOMEPAGE")
myLabel = Label(root, text="General User Interface", width = 50, height = 8, fg = "red")
myLabel.pack()






def memory():
    import memory
    myButton.pack()

def speed():
    import speed
    myButton1.pack()

def visuo():
    import Vis
    myButton1.pack()


myButton = Button(root, text="MEMORY BATTERY:\nMemory Battery requires you to locate matching \n boxes, once complete you will be given a score out of 21\n (21 = 100%)",width = 50, height = 5, command=memory, fg="red", bg="black")
myButton.pack()

myLabe2 = Label(root, text=" ")
myLabe2.pack()

myButton1 = Button(root, text="SPEED BATTERY:\n Speed Battery requires you to click the red circle 10 times,\n once complete an average speed will be scored ", width = 50, height = 5,  command=speed, fg="red", bg="black")
myButton1.pack()

myLabe4 = Label(root, text=" ")
myLabe4.pack()

myButton2 = Button(root, text="VISUOSPATIAL BATTERY:\nVisuospatial Battery requires you to hit targets,\nthe first 3 shots are not counted. Following this a mark out of 10 will be provided\n (10=100%)", width = 50, height = 5,  command=visuo, fg="red", bg="black")
myButton2.pack()

myLabe5 = Label(root, text=" ")
myLabe5.pack()

myButton3 = Button(root, text="DATABASE:\n Database will show you your previous scores", width = 50, height = 5,  command=visuo, fg="red", bg="black")
myButton3.pack()




root.mainloop()