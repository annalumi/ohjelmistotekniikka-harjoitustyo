from tkinter import ttk, StringVar, constants
from services.shop_service import shop_service, UsernameExistsError

class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_safety_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_safety = self._password_safety_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Käyttäjätunnus ja salasana vaaditaan")
            return
        if password != password_safety:
            self._show_error("Salasanat eivät ole samat")
            
        try:
            shop_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error("Käyttäjätunnus on jo olemassa")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field_safety(self):
        password_safety_label = ttk.Label(master=self._frame, text="Salasana uudestaan")

        self._password_safety_entry = ttk.Entry(master=self._frame)

        password_safety_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_safety_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_password_field_safety()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._create_user_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()