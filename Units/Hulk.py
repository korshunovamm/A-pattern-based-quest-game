from Units.Character import Character


class HulkClass(Character):
    def __init__(self):
        super().__init__('Hulk', intel=2, strength=10, flex=2, health=6)
