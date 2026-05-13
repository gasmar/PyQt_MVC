import sys

from PyQt6.QtWidgets import QApplication

from models.character_model import CharacterModel
from views.main_window import MainWindow
from controllers.character_controller import CharacterController


def main():
    app = QApplication(sys.argv)

    model = CharacterModel()
    view = MainWindow()
    controller = CharacterController(model, view)

    view.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()