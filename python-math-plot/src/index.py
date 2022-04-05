import tkinter as tk
from ui.math_view import MathView

math_window = MathView()

root =  tk.Tk()

math_window.mathview_create(root)

root.mainloop()


if __name__ == '__main__':
    main()