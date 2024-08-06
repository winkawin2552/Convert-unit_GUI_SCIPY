from scipy import constants
from tkinter import *
from tkinter import ttk 

Metric = {"zepto":constants.zepto, "atto":constants.atto, "femto":constants.femto, "pico":constants.pico, "nano":constants.nano, "micro":constants.micro, "milli":constants.milli, "centi":constants.centi, "deka":constants.deka, "hecto":constants.hecto, "kilo":constants.kilo, "mega":constants.mega, "giga":constants.giga, "tera":constants.tera, "peta":constants.peta, "exa":constants.exa, "zetta":constants.zetta, "yotta":constants.yotta}
Length = {"inch":constants.inch, "foot":constants.foot, "yard":constants.yard, "mile":constants.mile, "mil":constants.mil, "pt":constants.pt, "point":constants.point, "survey_foot":constants.survey_foot, "survey_mile":constants.survey_mile, "nautical_mile":constants.nautical_mile, "fermi":constants.fermi, "angstrom":constants.angstrom, "micron":constants.micron, "au":constants.au, "astronomical_unit":constants.astronomical_unit, "light_year":constants.light_year, "parsec":constants.parsec}
Time = {"minute":constants.minute, "hour":constants.hour, "day":constants.day, "week":constants.week, "year":constants.year, "Julian_year":constants.Julian_year}
Speed = {"kmh":constants.kmh, "mph":constants.mph, "mach":constants.mach, "speed_of_sound":constants.speed_of_sound, "knot":constants.knot}
Volume = {"liter":constants.liter, "litre":constants.litre, "gallon":constants.gallon, "gallon_US":constants.gallon_US, "gallon_imp":constants.gallon_imp, "fluid_ounce":constants.fluid_ounce, "fluid_ounce_US":constants.fluid_ounce_US, "fluid_ounce_imp":constants.fluid_ounce_imp, "barrel":constants.barrel, "bbl":constants.bbl}


def checkMode(event):
    if(mode.get() == "Metric"):
        options = ("zepto","atto","femto","pico","nano","micro","milli","centi","deka","hecto","kilo","mega","giga","tera","peta","exa","zetta","yotta")
    elif(mode.get() == "Length"):
        options = ("inch","foot","yard","mile","mil","pt","point","survey_foot","survey_mile","nautical_mile","fermi","angstrom","micron",
    "au","astronomical_unit","light_year","parsec"
)
    elif(mode.get() == "Time"):
        options = ("minute","hour","day","week","year","Julian_year")
    elif(mode.get() == "Speed"):
        options = ("kmh","mph","mach","speed_of_sound","knot")
    elif(mode.get() == "Volume"):
        options = ("liter","litre","gallon","gallon_US","gallon_imp","fluid_ounce","fluid_ounce_US","fluid_ounce_imp","barrel","bbl")
    else:
        options = ()
    changeUnit["values"] =options
    unit["values"] = options
    changeUnit.set("")
    print(mode.get())


def calculated():
    try:
        value = float(numEntry.get())
        print(numEntry.get())
        if(mode.get() == "Metric"):
            calculate  = (value * Metric[unit.get()])/Metric[changeUnit.get()]
        if(mode.get() == "Length"):
            calculate  = (value * Length[unit.get()])/Length[changeUnit.get()]
        if(mode.get() == "Time"):
            calculate  = (value * Time[unit.get()])/Time[changeUnit.get()]
        if(mode.get() == "Speed"):
            calculate  = (value * Speed[unit.get()])/Speed[changeUnit.get()]
        if(mode.get() == "Volume"):
            calculate  = (value * Volume[unit.get()])/Volume[changeUnit.get()]
        solution.set(f"{calculate:.2f} {changeUnit.get()}")   
    except(Exception):
        solution.set(f"Error: {Exception}") 

root = Tk()
root.title("การเปลี่ยนหน่วย")
root.configure(background="grey66")
root.geometry("405x350+100+100")

numLabel = Label(text= "Enter number")
numLabel.grid(row = 0, column=0, columnspan=3)


unitImg = PhotoImage(file = "picture/unit.png")
modeImg = PhotoImage(file = "picture/mode.png")


numEntry = Entry(root, width= 45, textvariable= StringVar())
numEntry.grid(row = 1, column= 1,ipady = 7)

labelUnit = Label(image= unitImg)
labelMode = Label(image= modeImg)
labelMode.grid(row =2,  pady=2)
labelUnit.grid(row = 3, pady = 5)

mode = ttk.Combobox(root, width = 27, textvariable = StringVar())
mode["values"] = ("Metric",
                  "Length",
                  "Time",
                  "Speed",
                  "Volume")
mode.grid(row = 2, column=1)
mode.bind("<<ComboboxSelected>>", checkMode)

unit = ttk.Combobox(root, width= 27, textvariable= StringVar())
unit.grid(row = 3, column=1)


labelChange = Label(text="Change To: ")
labelChange.grid(row = 4, column=0)

changeUnit = ttk.Combobox(root, width=27, textvariable=StringVar())
options =()
changeUnit.grid(row = 4, column=1)

calculatebutton = Button(root, text="Calculate", command= calculated)
calculatebutton.grid(row = 4, column=2)

resultLabel = Label(text="Your ResultL:")
resultLabel.grid(row = 5, column=0, pady=10, columnspan=2)

solution = StringVar()
solutionLabel = Label(root, textvariable= solution)
solutionLabel.grid(row= 6, column=0, columnspan=2, ipadx=100, ipady=20, pady = 10)

root.mainloop()