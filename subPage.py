from tkinter import *

def makeWindow(unit):
    root =Tk()
    root.geometry("499x281+530+250")
    root.title(unit)
    root.minsize(499, 281)
    root.maxsize(499, 281)
    unitPic = PhotoImage(file="picture/unit.png")

    backgroundIMG = PhotoImage(file="picture/background.png")
    canvas = Canvas(root, width=499, height=281, highlightthickness=0)

    canvas.grid(row=0, column=0, rowspan=5, columnspan=5)
    canvas.create_image(0, 0, anchor=NW, image=backgroundIMG)

    canvas.create_image(5, 5, anchor=NW, image=unitPic, tags="unitPic")

    root.mainloop()

def lenght(event):
    makeWindow("lenght")

def metric(event):
    makeWindow("metric")

def speed(event):
    makeWindow("speed")

def time(event):
    makeWindow("time")

def volume(event):
    makeWindow("volume")