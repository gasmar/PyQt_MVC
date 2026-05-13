class CharacterController:
    """
    Connects the model to the view.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.setup_model()
        self.connect_signals()

    def setup_model(self):
        self.view.character_list.setModel(self.model)

    def connect_signals(self):
        self.view.add_button.clicked.connect(
            self.add_character
        )
        self.view.character_list.clicked.connect(
            self.on_character_select
        )

    def add_character(self):
        name = self.view.character_input.text()

        self.model.add_character(name)

        self.view.character_input.clear()

    def on_character_select(self, index):
        character_name = self.model.data(index)
        self.view.selected_label.setText(
            f"Selected: {character_name}"
        )
