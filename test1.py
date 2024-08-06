from tkinter import *
from tkinter import ttk
from scipy import constants


def makeWindow(unit):
    Metric = {"zepto": constants.zepto, "atto": constants.atto, "femto": constants.femto, "pico": constants.pico, 
              "nano": constants.nano, "micro": constants.micro, "milli": constants.milli, "centi": constants.centi, 
              "deka": constants.deka, "hecto": constants.hecto, "kilo": constants.kilo, "mega": constants.mega, 
              "giga": constants.giga, "tera": constants.tera, "peta": constants.peta, "exa": constants.exa, 
              "zetta": constants.zetta, "yotta": constants.yotta}
    Length = {"inch": constants.inch, "foot": constants.foot, "yard": constants.yard, "mile": constants.mile, 
              "mil": constants.mil, "pt": constants.pt, "point": constants.point, "survey_foot": constants.survey_foot, 
              "survey_mile": constants.survey_mile, "nautical_mile": constants.nautical_mile, "fermi": constants.fermi, 
              "angstrom": constants.angstrom, "micron": constants.micron, "au": constants.au, 
              "astronomical_unit": constants.astronomical_unit, "light_year": constants.light_year, "parsec": constants.parsec}
    Time = {"minute": constants.minute, "hour": constants.hour, "day": constants.day, "week": constants.week, 
            "year": constants.year, "Julian_year": constants.Julian_year}
    Speed = {"kmh": constants.kmh, "mph": constants.mph, "mach": constants.mach, "speed_of_sound": constants.speed_of_sound, 
             "knot": constants.knot}
    Volume = {"liter": constants.liter, "litre": constants.litre, "gallon": constants.gallon, "gallon_US": constants.gallon_US, 
              "gallon_imp": constants.gallon_imp, "fluid_ounce": constants.fluid_ounce, "fluid_ounce_US": constants.fluid_ounce_US, 
              "fluid_ounce_imp": constants.fluid_ounce_imp, "barrel": constants.barrel, "bbl": constants.bbl}
    
    root = Tk()
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
    entryLabel.grid(row=0, column=0)
    entrybox = Entry(width=40, textvariable=StringVar())
    entrybox.grid(column=1, row=0, ipady=10)
    
    unitLabel = Label(text="First Unit:")
    unitLabel.grid(row=1, column=0)
    unitcombo = ttk.Combobox(root, width=27, textvariable=StringVar())
    unitcombo.grid(row=1, column=1)
    
    changLabel = Label(text="Change To:")
    changLabel.grid(row=2, column=0)
    changcombo = ttk.Combobox(root, width=27, textvariable=StringVar())
    changcombo.grid(row=2, column=1)
    
    resultText = StringVar()
    resultLabel = Label(textvariable=resultText)
    resultLabel.grid(row=3, column=1)
    
    def calculate_conversion():
        try:
            value = float(entrybox.get())
            from_unit = unitcombo.get()
            to_unit = changcombo.get()
            
            if unit == "Metric":
                calculate = (value * Metric[from_unit]) / Metric[to_unit]
            elif unit == "Length":
                calculate = (value * Length[from_unit]) / Length[to_unit]
            elif unit == "Time":
                calculate = (value * Time[from_unit]) / Time[to_unit]
            elif unit == "Speed":
                calculate = (value * Speed[from_unit]) / Speed[to_unit]
            elif unit == "Volume":
                calculate = (value * Volume[from_unit]) / Volume[to_unit]
            else:
                resultText.set("Invalid unit type")
                return
            
            resultText.set(f"{calculate:.2f} {to_unit}")
        except Exception as e:
            resultText.set(f"Error: {str(e)}")
    
    calculateBut = Button(text="Calculate", command=calculate_conversion)
    calculateBut.grid(row=3, column=2)
    
    options = {
        "Metric": ("zepto", "atto", "femto", "pico", "nano", "micro", "milli", "centi", "deka", "hecto", "kilo", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta"),
        "Length": ("inch", "foot", "yard", "mile", "mil", "pt", "point", "survey_foot", "survey_mile", "nautical_mile", "fermi", "angstrom", "micron", "au", "astronomical_unit", "light_year", "parsec"),
        "Time": ("minute", "hour", "day", "week", "year", "Julian_year"),
        "Speed": ("kmh", "mph", "mach", "speed_of_sound", "knot"),
        "Volume": ("liter", "litre", "gallon", "gallon_US", "gallon_imp", "fluid_ounce", "fluid_ounce_US", "fluid_ounce_imp", "barrel", "bbl")
    }
    
    unitcombo["values"] = options.get(unit, ())
    changcombo["values"] = options.get(unit, ())
    unitcombo.set("")
    changcombo.set("")
    
    root.mainloop()
