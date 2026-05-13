from PyQt6.QtCore import pyqtSignal, QObject, QModelIndex, Qt, QAbstractListModel


class CharacterModel(QAbstractListModel):
    """
    Stores character asset data.
    Emits a signal when the data changes.
    """


    characters_changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.characters = [
            "Knight",
            "Archer",
            "Wizard",
            "Goblin",
            "Dragon",
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self.characters)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return self.characters[index.row()]

        return None

    def get_characters(self):
        return self.characters

    def add_character(self, name):
        if not name:
            return

        row = len(self.characters)

        self.beginInsertRows(QModelIndex(), row, row)
        self.characters.append(name)
        self.endInsertRows()