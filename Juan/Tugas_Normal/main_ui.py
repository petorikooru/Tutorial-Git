from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowTitle("Hyperlink to Websites")
        Form.resize(300, 200)

        # Layout utama
        self.layout = QVBoxLayout(Form)

        # Label judul
        self.label = QLabel("Klik tombol untuk membuka situs web:")
        self.layout.addWidget(self.label)

        # Tombol hyperlink
        self.button_google = QPushButton("Open Google")
        self.layout.addWidget(self.button_google)

        self.button_youtube = QPushButton("Open YouTube")
        self.layout.addWidget(self.button_youtube)

        self.button_github = QPushButton("Open GitHub")
        self.layout.addWidget(self.button_github)

        self.button_w3schools = QPushButton("Open W3Schools")
        self.layout.addWidget(self.button_w3schools)
