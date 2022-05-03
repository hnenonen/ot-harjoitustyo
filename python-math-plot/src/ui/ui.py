from ui.login_view import LoginView
from ui.math_view import MathView
from ui.create_user_view import CreateView

class UI:
    """Class that is responsibe of programm UI
    """
    def __init__(self, root):
        """Class constructor. Creates a new Object responsible of the UI.

        Args:
            root: element from Tkinter library in which the UI is initialized.
        """   
        self._root = root
        self._current_view = None

    def start(self):
        """Start the UI
        """
        self._show_login_view()

    def _hide_current_view(self):
        """Hides the current view by destroying it
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _handle_math_view(self):
        """Opens a MathView window from LoginView window when pressed "Login"
        """
        self._hide_current_view()
        self._current_view = MathView(
            self._root)

    def _handle_create_user_view(self):
        """Opens a CreateView window from LoginView window when pressed "Create User"
        """
        self._hide_current_view()
        self._current_view = CreateView(
            self._root,
            self._show_login_view)

        self._current_view.pack()

    def _show_login_view(self):
        """Opening view for UI when programm starts.
            When in CreateView window it opens a LoginView window when pressed "Create User"
        """
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_math_view,
            self._handle_create_user_view
        )

        self._current_view.pack()

