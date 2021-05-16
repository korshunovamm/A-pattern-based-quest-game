class Character:
    def __init__(self, name, intel, strength, flex, health):
        self.name = name
        self.intel = intel
        self.strength = strength
        self.flex = flex
        self.health = health

    def __str__(self):
        return f'{self.name} (intel: {self.intel}, strength: {self.strength},' \
               f' flex: {self.flex}, health: {self.health})'
