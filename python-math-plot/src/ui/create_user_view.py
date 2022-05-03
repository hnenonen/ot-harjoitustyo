from tkinter import ttk

class CreateView:
    """Class that is responsible of the UI view of creating a new user.
    """
    def __init__(self, root, handle_create_view):
        """Class constructor. Creates a window for creating a new user.

        Args:
            root: Tkinter element in which the view is initialized.
            handle_create_view: Value to be called when moving to LoginView after creating a new user.
        """
        self.handle_create_view = handle_create_view
        self._root = root
        self._frame = None

        self._initialize()  

    def destroy(self):
        """Destroys the view
        """
        self._frame.destroy()

    def _initialize(self):   
        """Texts boxes for user entry, Labels to guide user and Buttons to execute are defined and initialized here to be packed.
        """
        self._frame = ttk.Frame(master=self._root)
        
        zero_label = ttk.Label(master=self._frame, text='Create new user')
        first_label = ttk.Label(master=self._frame, text='username')  
        username = ttk.Entry(master=self._frame)       
        second_label = ttk.Label(master=self._frame, text='password')
        password = ttk.Entry(master=self._frame)
    
        create_user_button = ttk.Button(master=self._frame, text="Create User",
                                command=self.handle_create_view)
    

        zero_label.grid(row=0, column=1)
        first_label.grid(row=1, column=0)
        username.grid(row=1, column=1)
        second_label.grid(row=2, column=0)
        password.grid(row=2, column=1)
        create_user_button.grid(row=3, column=1)

    def pack(self):
        """Show the CreateView window
        """
        self._frame.pack()