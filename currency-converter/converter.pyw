# Project #1 Currency Converter

import os
import tkinter as tk
from PIL import ImageTk
import decimal

base_folder = os.path.dirname(__file__)

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.resizable(0, 0)
        
        self.iconphoto(False, ImageTk.PhotoImage(file=os.path.join(base_folder, 'icon.png')))

        self.__canvas = tk.Canvas(self, bg="#000000", width=300, height=300)
        self.__canvas.pack_propagate(0)

        # backkground
        self.__bg = ImageTk.PhotoImage(file=os.path.join(base_folder, 'bg.png'))
        self.__canvas.create_image((150, 150), image=self.__bg)

        # text in screen
        self.__text_amount = self.__canvas.create_text((90, 40), font="Times 15 bold", 
            fill='white', text="Amount to convert:")
        self.__canvas.create_text((100, 75), font="Times 15 bold", fill='white', 
            text="Conversion rate:")
        self.__canvas.create_text((150, 120), font="Times 15 bold", fill='white', 
            text="Converted amount")

        self.__canvas_result = self.__canvas.create_text((150, 150), font="Times 15 bold", text="")

        # inputs
        self.__amount_input = tk.Entry(self.__canvas, width=18)
        self.__amount_input.place(x=180, y=30)

        self.__rate_input = tk.Entry(self.__canvas, width=18)
        self.__rate_input.place(x=180, y=65)

        # buttons
        self.__convert_btn = tk.Button(self.__canvas, text="Convert", bg="#E8C01A", font=("14"),
            fg="black", command=self.convert)
        self.__convert_btn.place(x=20, y=200)
        self.__convert_btn = tk.Button(self.__canvas, text="Clear", bg="#F75534", font=("14"),
            fg="white", command=self.clear)
        self.__convert_btn.place(x=230, y=200)

        self.__canvas.pack()

    def convert(self):
        """
        Convert amount from a currency to another one.
        """
        self.__canvas.delete(self.__canvas_result)  # Delete result 
        __amount = self.__amount_input.get()
        __rate = self.__rate_input.get()

        try:  # Catch the error in case the entries are not numeric. 
            __amount_total = decimal.Decimal(__amount) * decimal.Decimal(__rate)
            self.__canvas_result = self.__canvas.create_text((150, 150), font="Times 15 bold",
            fill='#E8C01A', text=__amount_total)
        except:
            if not __amount.isdigit():
                self.__canvas.create_text((150, 150), font="Times 15 bold",
                fill='#F75534', text="Invalid Amount")
            else:
                self.__canvas.create_text((150, 150), font="Times 15 bold",
                fill='#F75534', text="Invalid Rate")

    def clear(self):
        """
        Clear input widgets and display result text.
        """
        self.__canvas.delete(self.__canvas_result)
        self.__rate_input.delete(0, tk.END)
        self.__amount_input.delete(0, tk.END)


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.mainloop()
        
        