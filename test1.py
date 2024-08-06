from tkinter import *
from PIL import Image, ImageTk

def resize(img_path, size):
    image = Image.open(img_path)
    resize_image = image.resize(size)
    img = ImageTk.PhotoImage(resize_image)
    return img

# Load the image outside of the function to keep a reference
unitPic = resize("picture/unit.png", (50, 50))

def makeWindow(unit):
    root = Tk()
    root.geometry("499x281")
    root.minsize(499, 281)
    root.maxsize(499, 281)

    backgroundIMG = PhotoImage(file="picture/background.png")
    canvas = Canvas(root, width=499, height=281, highlightthickness=0)
    canvas.grid(row=0, column=0, rowspan=5, columnspan=5)
    canvas.create_image(0, 0, anchor=NW, image=backgroundIMG)

    # Create image with a unique identifier
    united = canvas.create_image(5, 5, anchor=NW, image=unit)

    # Keep a reference to the image to prevent garbage collection
    canvas.image = unit

    root.mainloop()

makeWindow(unitPic)
