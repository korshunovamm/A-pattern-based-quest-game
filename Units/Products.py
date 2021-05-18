from Creators import Character


class SherlockHolmesClass(Character):
    def __init__(self):
        super().__init__('SherlockHolmes', 2, 10, 2, 6)


class HulkClass(Character):
    def __init__(self):
        super().__init__('Hulk', 10, 2, 3, 5)


class SpidermanClass(Character):
    def __init__(self):
        super().__init__('Spider', 3, 3, 10, 4)


class JesusClass(Character):
    def __init__(self):
        super().__init__('Jesus', 5, 2, 3, 10)
