from tkinter import *
from tkinter import ttk
from scipy import constants
from ttkthemes import ThemedTk
import mainPage



def makeWindow(unit):
    def calculate():
        try:
            value = float(entrybox.get())
            if(unit == "Metric"):
                calculate  = (value * Metric[unitcombo.get()])/Metric[changecombo.get()]
            if(unit == "Length"):
                calculate  = (value * Length[unitcombo.get()])/Length[changecombo.get()]
            if(unit == "Time"):
                calculate  = (value * Time[unitcombo.get()])/Time[changecombo.get()]
            if(unit == "Speed"):
                calculate  = (value * Speed[unitcombo.get()])/Speed[changecombo.get()]
            if(unit == "Volume"):
                calculate  = (value * Volume[unitcombo.get()])/Volume[changecombo.get()]
            resultText.set(f"{calculate} {changecombo.get()}")   
        except(Exception):
            resultText.set(f"Error: {Exception}") 

    Metric = {"zepto":constants.zepto, "atto":constants.atto, "femto":constants.femto, "pico":constants.pico, "nano":constants.nano, "micro":constants.micro, "milli":constants.milli, "centi":constants.centi, "deka":constants.deka, "hecto":constants.hecto, "kilo":constants.kilo, "mega":constants.mega, "giga":constants.giga, "tera":constants.tera, "peta":constants.peta, "exa":constants.exa, "zetta":constants.zetta, "yotta":constants.yotta}
    Length = {"inch":constants.inch, "foot":constants.foot, "yard":constants.yard, "mile":constants.mile, "mil":constants.mil, "pt":constants.pt, "point":constants.point, "survey_foot":constants.survey_foot, "survey_mile":constants.survey_mile, "nautical_mile":constants.nautical_mile, "fermi":constants.fermi, "angstrom":constants.angstrom, "micron":constants.micron, "au":constants.au, "astronomical_unit":constants.astronomical_unit, "light_year":constants.light_year, "parsec":constants.parsec}
    Time = {"minute":constants.minute, "hour":constants.hour, "day":constants.day, "week":constants.week, "year":constants.year, "Julian_year":constants.Julian_year}
    Speed = {"kmh":constants.kmh, "mph":constants.mph, "mach":constants.mach, "speed_of_sound":constants.speed_of_sound, "knot":constants.knot}
    Volume = {"liter":constants.liter, "litre":constants.litre, "gallon":constants.gallon, "gallon_US":constants.gallon_US, "gallon_imp":constants.gallon_imp, "fluid_ounce":constants.fluid_ounce, "fluid_ounce_US":constants.fluid_ounce_US, "fluid_ounce_imp":constants.fluid_ounce_imp, "barrel":constants.barrel, "bbl":constants.bbl}
    
    def back():
        root.destroy()
        mainPage.main("")

    root = ThemedTk(theme="breeze")
    root.geometry("499x281+530+250")
    root.title(unit)
    root.minsize(499, 281)
    root.maxsize(499, 281)
    unitPic = PhotoImage(file="picture/unit.png")

    backgroundIMG = PhotoImage(file="picture/background.png")
    canvas = Canvas(root, width=499, height=281, highlightthickness=0)

    canvas.grid(row=0, column=0, rowspan=5, columnspan=5)
    canvas.create_image(0, 0, anchor=NW, image=backgroundIMG)

    canvas.create_image(444, 5, anchor=NW, image=unitPic, tags="unitPic")
    color = "linen"
    
    entryLabel = Label(text="Entry Number:", bg = color)
    entryLabel.grid(row = 0, column=0, ipadx=5, ipady=3)
    entrybox = Entry(width=40, textvariable= StringVar(), bg = "PeachPuff2")
    entrybox.grid(row =0, column=1, ipady = 10, sticky=W, padx=20)

    options = ()

    unitLabel = Label(text="First Unit:", bg = color)
    unitLabel.grid(row =1, column=0, ipadx=17, ipady=3)
    unitcombo = ttk.Combobox(root, width= 27, textvariable= StringVar())
    unitcombo.grid(row=1, column=1, sticky=W, padx=20)

    changeLabel = Label(text="change To:", bg = color)
    changeLabel.grid(row = 2, column=0, ipadx=17, ipady=3)
    changecombo = ttk.Combobox(root, width= 27, textvariable= StringVar())
    changecombo.grid(row=2, column=1, sticky=W, padx=20)

    resultText = StringVar()
    resultText.set("Your Result")
    resultLabel = Label(root, textvariable= resultText, bg = "PeachPuff1")
    resultLabel.grid(row=3, column=1, ipadx=70, ipady=5, sticky=W, padx=20)

    calculateBut = Button(text="Calculate", command= calculate, bg = "lemon chiffon", relief=RIDGE)
    calculateBut.grid(row = 3, column=0, ipadx=17)

    reverseImg = PhotoImage(file="picture/reverse.png")
    reverseBut = Button(image=reverseImg, width=30, height=30, command= back, relief=RIDGE)
    reverseBut.place(x = 444, y = 230)

    if(unit == "Metric"):
        options = ("zepto","atto","femto","pico","nano","micro","milli","centi","deka","hecto","kilo","mega","giga","tera","peta","exa","zetta","yotta")
    elif(unit == "Length"):
        options = ("inch","foot","yard","mile","mil","pt","point","survey_foot","survey_mile","nautical_mile","fermi","angstrom","micron",
    "au","astronomical_unit","light_year","parsec")
    elif(unit == "Time"):
        options = ("minute","hour","day","week","year","Julian_year")
    elif(unit == "Speed"):
        options = ("kmh","mph","mach","speed_of_sound","knot")
    elif(unit == "Volume"):
        options = ("liter","litre","gallon","gallon_US","gallon_imp","fluid_ounce","fluid_ounce_US","fluid_ounce_imp","barrel","bbl")
    else:
        options = ()
    unitcombo["values"] = options
    changecombo["values"] = options
    unitcombo.set("")
    changecombo.set("")


    root.mainloop()

def lenght(event):
    makeWindow("Length")

def metric(event):
    makeWindow("Metric")

def speed(event):
    makeWindow("Speed")

def time(event):
    makeWindow("Time")

def volume(event):
    makeWindow("Volume")

if __name__== "__main__":
    makeWindow("Speed")