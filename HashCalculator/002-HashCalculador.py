# Hash Calculator
# by: Jean Estevez https://github.com/Jean-carje

import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 
import hashlib


BLACK = "#000"
GRAY = "#b5b5b5"
GRAY_LINE = "#8a8888"
WITHE = "#fff"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Hash Tool")
        self.geometry("400x400")
        self.resizable(False, False)
        self.configure(bg=GRAY)
        self.option_add("*tk.Label.Font", "aerial 11 bold")
        self.option_add("*tk.Entry.Font", "aerial 11")
        self.option_add("*tk.Button.Font", "aerial 12 bold")
        
        self.widgets()
    
    def widgets(self):
        # FILE ----------------------------------------------
        self.label_file_explorer = tk.Label(self,  
                            text = "File",   
                            fg = BLACK, bg=GRAY)
        self.label_file_explorer.grid(row=0, column=0) 

        self.entry_file_explorer = tk.Entry(self, width=32)
        self.entry_file_explorer.grid(row=0, column=1) 

        self.btn_file_explorer = tk.Button(self,
                            text="...",
                            command=lambda: self.browseFiles(self.entry_file_explorer))
        self.btn_file_explorer.grid(row=0, column=2, pady=1, padx=1)  

        # FILE 2 --------------------------------------------
        self.label_file_explorer2 = tk.Label(self,  
                            text = "File",   
                            fg = BLACK, bg=GRAY)
        self.label_file_explorer2.grid(row=1, column=0) 

        self.entry_file_explorer2 = tk.Entry(self, width=32)
        self.entry_file_explorer2.grid(row=1, column=1) 

        self.btn_file_explorer2 = tk.Button(self,
                            text="...",
                            command=lambda: self.browseFiles(self.entry_file_explorer2))
        self.btn_file_explorer2.grid(row=1, column=2, pady=1, padx=2) 

        # BUTTONS -------------------------------------------
        self.btn_compare = tk.Button(self,
                            text="Compare",
                            command=self.compare_files)
        self.btn_compare.grid(row=2, column=1, pady=10, sticky=tk.W)
        self.btn_calculate = tk.Button(self,
                            text="Calculate",
                            command=self.calculate_file)
        self.btn_calculate.grid(row=2, column=1,pady=10, sticky=tk.E)

        # LABEL ---------------------------------------------

        self.label_text_compare = tk.Label(self, text="",
                                             bg=GRAY, 
                                             fg="green")
        self.label_text_compare.grid(row=3, column=1)

        # ---------------------------------------------------
        sep2 = tk.Frame(self, bg=GRAY_LINE, height=1, bd=0, width=400)
        sep2.grid(row=4, column=0, columnspan=4, sticky=tk.W, pady=5)

        # HASHING widgets -----------------------------------
        s = ttk.Style()
        s.configure("Style.TCheckbutton", background=GRAY, font="aerial 10 bold")

        self.check_md5 = ttk.Checkbutton(self, text="MD5", 
                                        style="Style.TCheckbutton",
                                        variable='')

        self.label_md5 = tk.Label(self, width=32)
        self.check_md4 = ttk.Checkbutton(self, text="MD4", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_md4 = tk.Label(self, width=32)
        self.check_sha1 = ttk.Checkbutton(self, text="SHA1", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_sha1 = tk.Label(self, width=32)
        self.check_sha224 = ttk.Checkbutton(self, text="SHA224", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_sha224 = tk.Label(self, width=32)
        self.check_sha256 = ttk.Checkbutton(self, text="SHA256", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_sha256 = tk.Label(self, width=32)
        self.check_sha384 = ttk.Checkbutton(self, text="SHA384", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_sha384 = tk.Label(self, width=32)
        self.check_sha512 = ttk.Checkbutton(self, text="SHA512", 
                                        style="Style.TCheckbutton", 
                                        variable='')
        self.label_sha512 = tk.Label(self, width=32)

        self.check_md5.grid(row=5, column=0, sticky=tk.W)
        self.check_md4.grid(row=6, column=0, sticky=tk.W)
        self.check_sha1.grid(row=7, column=0, sticky=tk.W)
        self.check_sha224.grid(row=8, column=0, sticky=tk.W)
        self.check_sha256.grid(row=9, column=0, sticky=tk.W)
        self.check_sha384.grid(row=10, column=0, sticky=tk.W)
        self.check_sha512.grid(row=11, column=0, sticky=tk.W)

        self.label_md5.grid(row=5, column=1, columnspan=3, pady=1)
        self.label_md4.grid(row=6, column=1, columnspan=4, pady=1)
        self.label_sha1.grid(row=7, column=1, columnspan=4, pady=1)
        self.label_sha224.grid(row=8, column=1, columnspan=4, pady=1)
        self.label_sha256.grid(row=9, column=1, columnspan=4, pady=1)
        self.label_sha384.grid(row=10, column=1, columnspan=4, pady=1)
        self.label_sha512.grid(row=11, column=1, columnspan=4, pady=1)

        # ---------------------------------------------------
        sep2 = tk.Frame(self, bg=GRAY_LINE, height=1, bd=0, width=400)
        sep2.grid(row=12, column=0, columnspan=3, sticky=tk.W, pady=5)

        # ---------------------------------------------------
        tk.Button(self, text="Clean", 
                    command=self.clean).grid(row=13, column=1, pady=8)
        tk.Button(self, text="Exit", 
                    command=self.destroy).grid(row=13, column=2, pady=8, padx=4)

    def browseFiles(self, widgt):
        """ Load file in label """
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 

        # insert direction in Entry widget
        widgt.delete(0, 'end')
        widgt.insert(0, filename) 

    def compare_files(self):
        """ Compare files with MD5 algorithm """
        rute1 = self.entry_file_explorer.get()
        rute2 = self.entry_file_explorer2.get()

        # calculate hash of two files
        try:
            with open(rute1, "rb") as f:
                one_value = self.generate_hash(self, f, hashlib.md5())
            with open(rute2, "rb") as f1:
                sec_value = self.generate_hash(self, f1, hashlib.md5())
        except FileNotFoundError:
            self.label_text_compare.configure(text="Select two files.")
            return

        # compare hash 
        if one_value == sec_value:
            self.label_text_compare.configure(text="True")
        else:
            self.label_text_compare.configure(text="False")

    def calculate_file(self):
        """ Calculate hash from file """
        rute = ""
        # get rute
        if len(self.entry_file_explorer.get()) > 1:
            rute = self.entry_file_explorer.get()
        else:
            rute = self.entry_file_explorer2.get()
        
        self.clean_label()  # clean labels

        try:
            with open(rute, "rb") as f:
                # open rute, generate hash and insert hash in label widget
                if self.check_md5.instate(['selected']):
                    self.label_md5.configure(text=self.generate_hash(f, hashlib.md5()))
                if self.check_md4.instate(['selected']):
                    data = f.read(2 ** 20)
                    hexObj = hashlib.new('md4', data)
                    self.label_md4.configure(text=hexObj.hexdigest())
                if self.check_sha1.instate(['selected']):    
                    self.label_sha1.configure(text=self.generate_hash(f, hashlib.sha1()))
                if self.check_sha224.instate(['selected']):    
                    self.label_sha224.configure(text=self.generate_hash(f, hashlib.sha224()))
                if self.check_sha256.instate(['selected']):    
                    self.label_sha256.configure(text=self.generate_hash(f, hashlib.sha256()))
                if self.check_sha384.instate(['selected']):    
                    self.label_sha384.configure(text=self.generate_hash(f, hashlib.sha384()))
                if self.check_sha512.instate(['selected']):    
                    self.label_sha512.configure(text=self.generate_hash(f, hashlib.sha512()))
        except FileNotFoundError:
            self.label_text_compare.configure(text="Select file.")

    def clean_label(self):
        """ clean hash labels """
        self.label_md5.configure(text="")
        self.label_md4.configure(text="")   
        self.label_sha1.configure(text="")
        self.label_sha224.configure(text="")
        self.label_sha256.configure(text="")
        self.label_sha384.configure(text="")
        self.label_sha512.configure(text="")

    def generate_hash(self, f, mode):
        """ 
            f: file 
            mode: hashlib algorithm     
        """
        while True:
            data = f.read(2 ** 20)
            if not data:
                break
            mode.update(data)
        return mode.hexdigest()

    def clean(self):
        """ clean all widgets """
        self.clean_label()  # clean labels
        self.entry_file_explorer.delete(0, 'end')
        self.entry_file_explorer2.delete(0, 'end')
        self.label_text_compare.configure(text="")

if __name__ == "__main__":
    app = App()
    app.mainloop()      