import webbrowser
from main_ui import Ui_Form


class MainController(Ui_Form):
    def __init__(self, Form):
        self.setupUi(Form)

        # Hubungkan tombol ke fungsi masing-masing
        self.button_google.clicked.connect(lambda: self.open_url("https://www.google.com"))
        self.button_youtube.clicked.connect(lambda: self.open_url("https://www.youtube.com"))
        self.button_github.clicked.connect(lambda: self.open_url("https://www.github.com"))
        self.button_w3schools.clicked.connect(lambda: self.open_url("https://www.w3schools.com"))

    def open_url(self, url):
        """Buka URL di browser default."""
        webbrowser.open(url)
