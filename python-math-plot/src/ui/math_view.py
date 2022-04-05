import tkinter as tk
from services.math_service import Approximate
from ui.ui import UIPlot

plot = UIPlot()
app = Approximate()

class MathView:    

    def mathview_create(self, root):
        root.geometry("600x400")

        first_label = tk.Label(root, text= 'Write function to be approximated')
        first_label.pack()
        second_label = tk.Label(root, text= 'exponents use ie. x**2 / exponental function ie. exp(x)')
        second_label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        my_button = tk.Button(root, text="graph it!", command=self.handle_button_click)
        my_button.pack()

    def handle_button_click(self):
        input = self.entry.get()
        if input == "":
            return

        func = app.define(input)
        taylor = app.taylor(func)
        graph = plot.plotting(func, taylor)

