from tkinter import E, ttk, constants

class LoginView:
    def __init__(self, root, handle_login_view):
        self._root = root
        self.handle_login_view = handle_login_view
        self._frame = None

        self._initialize()  

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Welcome to TaylorApp")

        entry = ttk.Entry(master=self._frame)
        

        button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self.handle_login_view
        )   

        label.grid(row=0, column=0)
        entry.grid(row=1, column=0)
        button.grid(row=2, column=0)


    def handle_button_click(self):
        self.entry.get()
        
    