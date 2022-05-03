from tkinter import ttk

class LoginView:
    def __init__(self, root, handle_login_view, handle_create_view):
        self._root = root
        self.handle_login_view = handle_login_view
        self.handle_create_view = handle_create_view
        self._frame = None

        self._initialize()  

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Welcome to TaylorApp")
        label_username = ttk.Label(master=self._frame, text="username")
        username = ttk.Entry(master=self._frame)

        password = ttk.Entry(master=self._frame)
        label_password = ttk.Label(master=self._frame, text="password")

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self.handle_login_view
        )   
        create_user_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self.handle_create_view
        )   

        label.grid(row=0, column=1)
        label_username.grid(row=1, column=0)
        username.grid(row=1, column=1)
        label_password.grid(row=2, column=0)
        password.grid(row=2, column=1)
        login_button.grid(row=3, column=1)
        create_user_button.grid(row=4, column=1)

    
    