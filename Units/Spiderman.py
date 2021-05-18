from Units.Character import Character


class SpidermanClass(Character):
    def __init__(self):
        super().__init__('Spider', intel=3, strength=3, flex=10, health=4)
