from ttkbootstrap import *

# Window
root = Window(themename='minty')
root.geometry('1000x700')
root.title('Binary and Decimal')

#Style
mystyle = Style()
mystyle.configure('danger.TButton', font=("Comic Sans MS", 18))

# Entry for input
E1 = Entry(root, font=('Trebuchet MS', 28, 'bold italic'), width=33)
E1.place(relx = 0.5, rely = 0.2, anchor='center')

# Class of Button
class NewButton:
    Bases = {"Hexadecimal": 16, "Octal": 8, "Decimal": 10, "Binary": 2} # Bases
    Styles = {"Hexadecimal": "warning",
              "Octal": "danger",
              "Decimal": "success",
              "Binary": "info"} # Colors

    # Initial
    def __init__(self, __base, __convert, __root):
        self.base = self.Bases[__base] # Number
        self.convert = self.Bases[__convert] # Number to convert to
        self.mystyle = Style() # Style
        self.mystyle.configure(f"{self.Styles[__base]}.TButton", font=("Comic Sans MS", 10)) # Style based on base
        # The button
        self.button = Button(__root, text=f'{__base} to {__convert}', style=f'{self.Styles[__base]}.TButton', command=self.Convert)

    # Convert (self.base --> self.convert)
    def Convert(self):
        if self.base == 16:
            if self.convert == 2:
                scale = int(E1.get(), 16)
                scale = str(bin(scale))
                L1.configure(text=(scale).removeprefix('0b'))

            elif self.convert == 8:
                scale = int(E1.get(), 16)
                scale = str(oct(scale))
                L1.configure(text=(scale).removeprefix('0o'))

            elif self.convert == 10:
                scale = int(E1.get(), 16)
                L1.configure(text=(scale))

        elif self.base == 8:
            if self.convert == 2:
                scale = int(E1.get(), 8)
                scale = str(bin(scale))
                L1.configure(text=(scale).removeprefix('0b'))

            elif self.convert == 16:
                scale = int(E1.get(), 8)
                scale = str(hex(scale)).upper()
                L1.configure(text=(scale).removeprefix('0X'))

            elif self.convert == 10:
                scale = int(E1.get(), 8)
                L1.configure(text=(scale))

        elif self.base == 2:
            if self.convert == 8:
                scale = int(E1.get(), 2)
                scale = str(oct(scale))
                L1.configure(text=(scale).removeprefix('0o'))

            elif self.convert == 16:
                scale = int(E1.get(), 2)
                scale = str(hex(scale)).upper()
                L1.configure(text=(scale).removeprefix('0X'))

            elif self.convert == 10:
                scale = int(E1.get(), 2)
                L1.configure(text=(scale))

        elif self.base == 10:
            if self.convert == 8:
                scale = str(oct(int(E1.get())))
                L1.configure(text=(scale).removeprefix('0o'))

            elif self.convert == 16:
                scale = str(hex(int(E1.get()))).upper()
                L1.configure(text=(scale).removeprefix('0X'))

            elif self.convert == 2:
                scale = str(bin(int(E1.get())))
                L1.configure(text=(scale).removeprefix('0b'))

# Label Frame 1
LF1 = Labelframe(root, text="Hexadecimals", labelanchor="nw", bootstyle="warning")
B1 = NewButton("Hexadecimal", "Binary", LF1)
B1.button.configure(width=19)
B1.button.pack(padx = 10, pady = 10)
B2 = NewButton("Hexadecimal", "Decimal", LF1)
B2.button.pack(padx = 10, pady = 10)
B3 = NewButton("Hexadecimal", "Octal", LF1)
B3.button.configure(width=19)
B3.button.pack(padx = 10, pady = 10)
LF1.place(relx = (1 / 8), rely = (0.45), anchor = "center")
LF2 = Labelframe(root, text="Octals", labelanchor="nw", bootstyle="danger")

# Label Frame 2
B4 = NewButton("Octal", "Binary", LF2)
B4.button.configure(width=18)
B4.button.pack(padx = 10, pady = 10)
B5 = NewButton("Octal", "Decimal", LF2)
B5.button.configure(width=18)
B5.button.pack(padx = 10, pady = 10)
B6 = NewButton("Octal", "Hexadecimal", LF2)
B6.button.configure(width=18)
B6.button.pack(padx = 10, pady = 10)
LF2.place(relx = (2.95 / 8), rely = (0.45), anchor = "center")

# Label Frame 3
LF3 = Labelframe(root, text="Decimals", labelanchor="nw", bootstyle="success")
B7 = NewButton("Decimal", "Binary", LF3)
B7.button.configure(width=20)
B7.button.pack(padx = 10, pady = 10)
B8 = NewButton("Decimal", "Octal", LF3)
B8.button.configure(width=20)
B8.button.pack(padx = 10, pady = 10)
B9 = NewButton("Decimal", "Hexadecimal", LF3)
B9.button.configure(width=20)
B9.button.pack(padx = 10, pady = 10)
LF3.place(relx = (4.95 / 8), rely = (0.45), anchor = "center")

# Label Frame 4
LF4 = Labelframe(root, text="Binaries", labelanchor="nw", bootstyle="info")
B10 = NewButton("Binary", "Decimal", LF4)
B10.button.configure(width=20)
B10.button.pack(padx = 10, pady = 10)
B11 = NewButton("Binary", "Octal", LF4)
B11.button.configure(width=20)
B11.button.pack(padx = 10, pady = 10)
B12 = NewButton("Binary", "Hexadecimal", LF4)
B12.button.configure(width=20)
B12.button.pack(padx = 10, pady = 10)
LF4.place(relx = (7 / 8), rely = (0.45), anchor = "center")
L1 = Label(root, text=0, font=("Trebuchet MS", 48, "bold italic"))
L1.place(relx = 0.5, rely = 0.75, anchor='center')


root.mainloop() # Mainloop()
