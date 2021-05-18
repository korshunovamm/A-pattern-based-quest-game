from UnitsCreators.CharacterCreator import CharacterCreator
from Units.Spiderman import SpidermanClass


class SpidermanCreator(CharacterCreator):
    def create(self):
        return SpidermanClass()
