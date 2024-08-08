from tkinter import *
from PIL import Image, ImageTk
import subPage

def main(event):
    root = Tk()
    root.geometry("499x281+530+250")
    root.minsize(499, 281)
    root.maxsize(499, 281)

    def lenghtMain(event):
        root.destroy()
        subPage.lenght("")
    def MetricMain(event):
        root.destroy()
        subPage.metric("")
    def SpeedMain(event):
        root.destroy()
        subPage.speed("")
    def TimeMain(event):
        root.destroy()
        subPage.time("")
    def VolumeMain(event):
        root.destroy()
        subPage.volume("")



    def resize(img_path, size):
        image = Image.open(img_path)
        resize_image = image.resize(size)
        img = ImageTk.PhotoImage(resize_image)
        return img


    metricPic = resize("picture/metric.png", (200, 200))
    lenghtPic = resize("picture/lenght.png", (200, 200))
    speedPic = resize("picture/speed.png", (200, 200))
    timePic = resize("picture/time.png", (200, 200))
    volumePic = resize("picture/volume.png", (200, 200))
    modePic = resize("picture/mode.png", (50, 50))

    canvas = Canvas(root, width=499, height=281, highlightthickness=0)
    canvas.grid(row=0, column=0, rowspan=5, columnspan=5)


    backgroundIMG = PhotoImage(file="picture/background.png")
    canvas.create_image(0, 0, anchor=NW, image=backgroundIMG)


    canvas.create_image(10, 0, anchor=NW, image=lenghtPic, tags="lenghtPic")
    canvas.create_image(160, 0, anchor=NW, image=metricPic, tags="metricPic")
    canvas.create_image(300, 0, anchor=NW, image=speedPic, tags="speedPic")
    canvas.create_image(10, 120, anchor=NW, image=timePic, tags="timePic")
    canvas.create_image(160, 120, anchor=NW, image=volumePic, tags="volumePic")
    canvas.create_image(5, 5, anchor=NW, image=modePic, tags="modePic")


    canvas.tag_bind("lenghtPic", "<Button-1>", lenghtMain)
    canvas.tag_bind("metricPic", "<Button-1>", MetricMain)
    canvas.tag_bind("speedPic", "<Button-1>", SpeedMain)
    canvas.tag_bind("timePic", "<Button-1>", TimeMain)
    canvas.tag_bind("volumePic", "<Button-1>", VolumeMain)

    root.mainloop()

if __name__ == "__main__":
    main("")