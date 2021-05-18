class Personality:
    def __init__(self, name):
        self.name = name


class CreatorPersonality(Personality):
    def factory(self):
        person_class = {
            "Hulk": HulkClass,
            "Hlms": SherlockHolmesClass,
            "Spider": SpidermanClass,
            "Jss": JesusClass
        }
        return person_class[self.name]()


class Character:
    def __init__(self, name, *args):
        self.name = name
        self.intel = args[0]
        self.strength = args[1]
        self.flex = args[2]
        self.health = args[3]

    def __str__(self):
        return f'{self.name} (intel: {self.intel}, strenght: {self.strength},' \
               f' flex: {self.flex}, health: {self.health})'


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


b = CreatorPersonality('Hulk').factory()
print(b.health)
print(b)
