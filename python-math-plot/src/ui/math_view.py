from tkinter import ttk
from services.math_service import Approximate
from ui.ui_plot import UIPlot

plot = UIPlot()
app = Approximate()


class MathView:
    
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()  

    def _initialize(self):   

        first_label = ttk.Label(text='Write function to be approximated')
        first_label.pack()
        second_label = ttk.Label(text='exponents use ie. x**2 / exponental function ie. exp(x)')
        second_label.pack()

        self.entry = ttk.Entry()
        self.entry.pack()

        my_button = ttk.Button(text="graph it!",
                                command=self.handle_button_click)
        my_button.pack()

    def destroy(self):
        self._frame.destroy()

    def handle_button_click(self):
        input = self.entry.get()
        if input == "":
            return

        func = app.define(input)
        taylor = app.taylor(func)

        plot.plotting(func, taylor)
