from Units.Creators import Character


class HulkClass(Character):
    def __init__(self):
        super().__init__('Hulk', intel=2, strength=10, flex=2, health=6)


class SherlockHolmesClass(Character):
    def __init__(self):
        super().__init__('SherlockHolmes', intel=10, strength=2, flex=3, health=5)


class SpidermanClass(Character):
    def __init__(self):
        super().__init__('Spider', intel=3, strength=3, flex=10, health=4)


class JesusClass(Character):
    def __init__(self):
        super().__init__('Jesus', intel=5, strength=2, flex=3, health=10)
