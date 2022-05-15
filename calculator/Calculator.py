# Calculator GUI with tkinter
# Day 01
# By Jean Estevez

import tkinter as tk
import math


# constants
BLACK = "#030303"
GRAY = "#b5b5b5"
ORANGE = "#f39c12"
RED = "#ff0008"

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.Font_tuple = ("Comic Sans MS", 10)

        self.title("Calculator")
        # self.iconphoto(False, tk.PhotoImage(file=ruta))

        self.geometry("234x400")
        self.resizable(False, False)
        self.configure(bg=BLACK)

        self.trigVal = tk.DoubleVar()
        self.isTrigVal = tk.BooleanVar()

        self.buttons()
        self.screenText()

    def buttons(self):
        """ Create Widgets of buttons in screen. """
        btn0 = tk.Button(self, bg=GRAY, width=12, height=2, text="0", command=lambda: self.setValue("0"))
        btn0.grid(row=9, column=0, columnspan=2, padx=3, pady=3)
        btn1 = tk.Button(self, bg=GRAY, width=6, height=2, text="1", command=lambda: self.setValue("1"))
        btn1.grid(row=8, column=0, padx=3, pady=3)
        btn2 = tk.Button(self, bg=GRAY, width=6, height=2, text="2", command=lambda: self.setValue("2"))
        btn2.grid(row=8, column=1, padx=3, pady=3)
        btn3 = tk.Button(self, bg=GRAY, width=6, height=2, text="3", command=lambda: self.setValue("3"))
        btn3.grid(row=8, column=2, padx=3, pady=3)
        btn4 = tk.Button(self, bg=GRAY, width=6, height=2, text="4", command=lambda: self.setValue("4"))
        btn4.grid(row=7, column=0, padx=3, pady=3)
        btn5 = tk.Button(self, bg=GRAY, width=6, height=2, text="5", command=lambda: self.setValue("5"))
        btn5.grid(row=7, column=1, padx=3, pady=3)
        btn6 = tk.Button(self, bg=GRAY, width=6, height=2, text="6", command=lambda: self.setValue("6"))
        btn6.grid(row=7, column=2, padx=3, pady=3)
        btn7 = tk.Button(self, bg=GRAY, width=6, height=2, text="7", command=lambda: self.setValue("7"))
        btn7.grid(row=6, column=0, padx=3, pady=3)
        btn8 = tk.Button(self, bg=GRAY, width=6, height=2, text="8", command=lambda: self.setValue("8"))
        btn8.grid(row=6, column=1, padx=3, pady=3)
        btn9 = tk.Button(self, bg=GRAY, width=6, height=2, text="9", command=lambda: self.setValue("9"))
        btn9.grid(row=6, column=2, padx=3, pady=3)
        btnDot = tk.Button(self, bg=GRAY, width=6, height=2, text=".", command=lambda: self.setValue("."))
        btnDot.grid(row=9, column=2, padx=3, pady=3)

        btnC = tk.Button(self, bg=GRAY, width=6, height=2, text="C", command=lambda: self.clean())
        btnC.grid(row=5, column=0, padx=3, pady=3)
        btnParentheses1 = tk.Button(self, bg=GRAY, width=6, height=2, text="(", command=lambda: self.setValue("("))
        btnParentheses1.grid(row=5, column=1, padx=3, pady=3)
        btnParentheses2 = tk.Button(self, bg=GRAY, width=6, height=2, text=")", command=lambda: self.setValue(")"))
        btnParentheses2.grid(row=5, column=2, padx=3, pady=3)

        btne = tk.Button(self, bg=GRAY, width=6, height=2, text="e", command=lambda: self.setValue(math.e))
        btne.grid(row=4, column=0, padx=3, pady=3)
        btnPI = tk.Button(self, bg=GRAY, width=6, height=2, text="π", command=lambda: self.setValue(math.pi))
        btnPI.grid(row=4, column=1, padx=3, pady=3)
        btnsin = tk.Button(self, bg=GRAY, width=6, height=2, text="sin", command=lambda: self.setValue("sin"))
        btnsin.grid(row=4, column=2, padx=3, pady=3)
        btndeg = tk.Button(self, bg=GRAY, width=6, height=2, text="deg", command=lambda: self.setValue("deg"))
        btndeg.grid(row=4, column=3, padx=3, pady=3)

        btnDiv = tk.Button(self, bg=ORANGE, width=6, height=2, text="/", command=lambda: self.setValue("/"))
        btnDiv.grid(row=5, column=3, padx=3, pady=3)
        btnMult = tk.Button(self, bg=ORANGE, width=6, height=2, text="*", command=lambda: self.setValue("*"))
        btnMult.grid(row=6, column=3, padx=3, pady=3)
        btnSub = tk.Button(self, bg=ORANGE, width=6, height=2, text="-", command=lambda: self.setValue("-"))
        btnSub.grid(row=7, column=3, padx=3, pady=3)
        btnAdd = tk.Button(self, bg=ORANGE, width=6, height=2, text="+", command=lambda: self.setValue("+"))
        btnAdd.grid(row=8, column=3, padx=3, pady=3)

        btnEqual = tk.Button(self, bg=RED, width=6, height=2, text="=", command=lambda: self.result())
        btnEqual.grid(row=9, column=3, padx=3, pady=3)

        for n in range(0, 10):
            self.bind(str(n), lambda el: self.setValue(el.char))
            self.bind(f"<KP_{n}>", lambda el: self.setValue(el.char))
        
        self.bind("*", lambda el: self.setValue(el.char))
        self.bind("/", lambda el: self.setValue(el.char))
        self.bind("+", lambda el: self.setValue(el.char))
        self.bind("-", lambda el: self.setValue(el.char))

        self.bind(".", lambda el: self.setValue(el.char))
        self.bind(",", lambda el: self.setValue("."))

        self.bind("(", lambda el: self.setValue(el.char))
        self.bind(")", lambda el: self.setValue(el.char))

        self.bind("=", lambda el: self.result())
        self.bind("c", lambda el: self.clean())
        self.bind("C", lambda el: self.clean())
    
    def screenText(self):
        """ Create widgets of text and entry widget. """
        self.textEntry = tk.Entry(self, bg=GRAY, fg=BLACK)
        self.textEntry.configure(font = self.Font_tuple, width=28, relief=tk.FLAT)
        self.textEntry.grid(row=2, column=0, columnspan=4, pady=(0, 5))

        self.textLabel = tk.Label(self, bg=GRAY, font=("Comic Sans MS", 10, "bold"))
        self.textLabel.configure(width=27, height=3, relief=tk.FLAT)
        self.textLabel.grid(row=0, rowspan=1, column=0, columnspan=4, pady=(5, 0))
    
    def setValue(self, val):
        """ Assign values to entry widget. """
        if val not in ["sin", "cos"]:
            self.textEntry.insert(tk.END, val)
            return

        if val == "sin":
            self.textEntry.insert(tk.END, "math.sin(")
        else:
            self.textEntry.insert(tk.END, "math.cos(")

    def result(self):
        """ Print result in LABEL widget. """
        try:
            temp = self.changeType(eval(self.textEntry.get()))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as err:
            temp = err.msg

        self.textLabel.configure(text=temp)
        self.textLabel.grid(row=0, rowspan=1, column=0, columnspan=4, pady=(5, 0))
        
    def clean(self):
        """ Clean ENTRY and LABEL widgets. """
        self.textEntry.delete(0, tk.END)

        self.textLabel.configure(text="")
        self.textLabel.grid(row=0, rowspan=1, column=0, columnspan=4, pady=(5, 0))

    def changeType(self, val):
        if isinstance(val, int):
            return int(val)
        elif isinstance(val, float):
            return float(val)
        else:
            return 0

       
if __name__ == "__main__":
    app = App()
    app.mainloop()