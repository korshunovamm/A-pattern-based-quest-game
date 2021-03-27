def setval(char_type):
    char_dict = {
        "Hulk": {'Intel': 2, 'Strength': 10, 'Flex': 3, 'Health': 7},
        "Hlms": {'Intel': 10, 'Strength': 2, 'Flex': 2, 'Health': 5},
        "Spider": {'Intel': 3, 'Strength': 2, 'Flex': 10, 'Health': 6},
        "Jss": {'Intel': 1, 'Strength': 2, 'Flex': 3, 'Health': 10},
        # "Ekz": {'Intel': 1, 'Strength': 2, 'Flex': 3, 'Health': 4, 'Luck': 5}
    }
    return char_dict[char_type]


def factory(char_type):
    types = {
        "Hulk": HulkClass,
        "Hlms": SherlockHolmsClass,
        "Spider": SpidermanClass,
        "Jss": JesusClass
    }
    return types[char_type]()


class Character:
    def __init__(self, char_dict):
        self.intel = char_dict['Intel']
        self.strength = char_dict['Strength']
        self.flex = char_dict['Flex']
        self.health = char_dict['Health']


class HulkClass(Character):
    def __init__(self):
        char_dict = setval(str(self))
        super().__init__(char_dict)

    def __str__(self):
        return 'Hulk'


class SherlockHolmsClass(Character):
    def __init__(self):
        char_dict = setval(str(self))
        super().__init__(char_dict)

    def __str__(self):
        return 'Hlms'


class SpidermanClass(Character):
    def __init__(self):
        char_dict = setval(str(self))
        super().__init__(char_dict)

    def __str__(self):
        return 'Spider'


class JesusClass(Character):
    def __init__(self):
        char_dict = setval(str(self))
        super().__init__(char_dict)

    def __str__(self):
        return 'Jss'
