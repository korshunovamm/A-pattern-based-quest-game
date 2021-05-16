from Units.Character import Character


class SherlockHolmesClass(Character):
    def __init__(self):
        super().__init__('SherlockHolmes', intel=10, strength=2, flex=3, health=5)