from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QListView, QLineEdit, QPushButton, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MVC Tutorial")

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Character list
        self.character_list = QListView()

        # Input field
        self.character_input = QLineEdit()
        self.character_input.setPlaceholderText("Enter character name...")

        # Add button
        self.add_button = QPushButton("Add Character")

        # Selected character label
        self.selected_label = QLabel("Select: None")

        # Add widgets to layout
        layout.addWidget(self.character_list)
        layout.addWidget(self.character_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.selected_label)
