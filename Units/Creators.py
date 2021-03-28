class Personality:
    def __init__(self, name):
        self.name = name


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
