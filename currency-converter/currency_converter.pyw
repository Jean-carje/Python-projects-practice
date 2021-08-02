""" Project #2 Currency Converter by Jean Estevez.
Currency converter online whit api (exchangerate) 
API: https://exchangerate.host/
"""

import os
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import decimal
import requests


SYMBOLS = 'https://api.exchangerate.host/symbols'
base_folder = os.path.dirname(__file__)


class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__data_convert = list(requests.get(SYMBOLS).json()["symbols"].keys())

        self.title("Currency Converter")
        self.resizable(0, 0)

        self._icon = ImageTk.PhotoImage(file=os.path.join(base_folder, 'icon.png'))
        self.iconphoto(False, self._icon)

        self.__canvas = tk.Canvas(self, bg="#000000", width=400, height=300)
        self.__canvas.pack_propagate(0)

        # ---------------------------------------------------------------------
        # Background
        self.__bg = ImageTk.PhotoImage(file=os.path.join(base_folder, 'bg.png'))
        self.__canvas.create_image((200, 150), image=self.__bg)

        # ---------------------------------------------------------------------
        # Text in screen
        self.__canvas.create_text((200, 40), font="Times 17 bold", fill='white', 
            text="Amount to convert:")
        self.__canvas.create_text((100, 105), font="Times 15 bold", fill='white', 
            text="from:")
        self.__canvas.create_text((300, 105), font="Times 15 bold", fill='white', 
            text="to:")

        self.__canvas_result = self.__canvas.create_text((200, 180),
            font="Times 18 bold", text="")

        # ---------------------------------------------------------------------
        # Input amount
        self.__amount_input = tk.Entry(self.__canvas, width=50)
        self.__amount_input.place(x=50, y=55)

        # ---------------------------------------------------------------------
        # Selection (from / to)
        self._from = ttk.Combobox(self, state="readonly", values=self.__data_convert,
            width=10)
        self._from.current(0)
        self._from.place(x=60, y=120)

        self._to = ttk.Combobox(self, state="readonly", values=self.__data_convert,
            width=10)
        self._to.current(0)
        self._to.place(x=260, y=120)

        # ---------------------------------------------------------------------
        # Buttons
        self.__convert_btn = tk.Button(self.__canvas, text="Convert", bg="#E8C01A", 
            font=("14"), fg="black", command=self.convert)
        self.__convert_btn.place(x=50, y=230)

        self.__convert_btn = tk.Button(self.__canvas, text="Clear", bg="#F75534",
            font=("14"), fg="white", command=self.clear_results)
        self.__convert_btn.place(x=300, y=230)

        # ---------------------------------------------------------------------
        self.__canvas.pack()

    def convert(self):
        """
        Convert amount from a currency to another one.
        """
        self.__canvas.delete(self.__canvas_result)  # Delete result in screen.

        url = f"https://api.exchangerate.host/latest?base={self._from.get()}"

        __amount = self.__amount_input.get()
        __rate = requests.get(url).json()["rates"][self._to.get()] # Exchange value

        try:  # Catch the error in case the (entries) are not numeric. 
            decimal.getcontext().prec = 5
            __amount_total = decimal.Decimal(__amount) * decimal.Decimal(__rate)
            
            self.__canvas_result = self.__canvas.create_text((200, 180), 
                font="Times 18 bold", fill='#E8C01A', text=__amount_total)
        except:
            if not __amount.isdigit():
                self.__canvas_result = self.__canvas.create_text((200, 180), 
                    font="Times 18 bold", fill='#F75534', text="Invalid Amount")
            else:
                self.__canvas_result = self.__canvas.create_text((200, 180),
                    font="Times 18 bold", fill='#F75534', text="Invalid Rate")

    def clear_results(self):
        """
        clear input widgets and display result text.
        """
        self.__canvas.delete(self.__canvas_result)  # clear results
        self.__amount_input.delete(0, tk.END)

        self._from.current(0)
        self._to.current(0)


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.mainloop()
       
        