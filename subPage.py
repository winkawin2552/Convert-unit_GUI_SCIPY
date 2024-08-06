from tkinter import *
from tkinter import ttk
from scipy import constants


def makeWindow(unit):
    def calculate():
        try:
            value = float(entrybox.get())
            print(entrybox.get())
            if(unit == "Metric"):
                calculate  = (value * Metric[unitcombo.get()])/Metric[changcombo.get()]
            if(unit == "Length"):
                calculate  = (value * Length[unitcombo.get()])/Length[changcombo.get()]
            if(unit == "Time"):
                calculate  = (value * Time[unitcombo.get()])/Time[changcombo.get()]
            if(unit == "Speed"):
                calculate  = (value * Speed[unitcombo.get()])/Speed[changcombo.get()]
            if(unit == "Volume"):
                calculate  = (value * Volume[unitcombo.get()])/Volume[changcombo.get()]
            resultText.set(f"{calculate:.2f} {changcombo.get()}")   
        except(Exception):
            resultText.set(f"Error: {Exception}") 

    Metric = {"zepto":constants.zepto, "atto":constants.atto, "femto":constants.femto, "pico":constants.pico, "nano":constants.nano, "micro":constants.micro, "milli":constants.milli, "centi":constants.centi, "deka":constants.deka, "hecto":constants.hecto, "kilo":constants.kilo, "mega":constants.mega, "giga":constants.giga, "tera":constants.tera, "peta":constants.peta, "exa":constants.exa, "zetta":constants.zetta, "yotta":constants.yotta}
    Length = {"inch":constants.inch, "foot":constants.foot, "yard":constants.yard, "mile":constants.mile, "mil":constants.mil, "pt":constants.pt, "point":constants.point, "survey_foot":constants.survey_foot, "survey_mile":constants.survey_mile, "nautical_mile":constants.nautical_mile, "fermi":constants.fermi, "angstrom":constants.angstrom, "micron":constants.micron, "au":constants.au, "astronomical_unit":constants.astronomical_unit, "light_year":constants.light_year, "parsec":constants.parsec}
    Time = {"minute":constants.minute, "hour":constants.hour, "day":constants.day, "week":constants.week, "year":constants.year, "Julian_year":constants.Julian_year}
    Speed = {"kmh":constants.kmh, "mph":constants.mph, "mach":constants.mach, "speed_of_sound":constants.speed_of_sound, "knot":constants.knot}
    Volume = {"liter":constants.liter, "litre":constants.litre, "gallon":constants.gallon, "gallon_US":constants.gallon_US, "gallon_imp":constants.gallon_imp, "fluid_ounce":constants.fluid_ounce, "fluid_ounce_US":constants.fluid_ounce_US, "fluid_ounce_imp":constants.fluid_ounce_imp, "barrel":constants.barrel, "bbl":constants.bbl}
    

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
    
    entryLabel = Label(text="Entry Number:")
    entryLabel.grid(row = 0, column=0)
    entrybox = Entry(width=40, textvariable= StringVar())
    entrybox.grid(column=1, row=0, ipady = 10)

    options = ()

    unitLabel = Label(text="First Unit:")
    unitLabel.grid(row =1, column=0)
    unitcombo = ttk.Combobox(root, width= 27, textvariable= StringVar())
    unitcombo.grid(row=1, column=1)

    changLabel = Label(text="Chang To:")
    changLabel.grid(row = 2, column=0)
    changcombo = ttk.Combobox(root, width= 27, textvariable= StringVar())
    changcombo.grid(row=2, column=1)

    resultText = StringVar()
    resultLabel = Label(root, textvariable= resultText)
    resultLabel.grid(row=3, column=1)

    calculateBut = Button(text="calculated", command= calculate )
    calculateBut.grid(row = 3, column=2)

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
    changcombo["values"] = options
    unitcombo.set("")
    changcombo.set("")


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