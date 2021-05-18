from UnitsCreators.CharacterCreator import CharacterCreator
from Units.Jesus import JesusClass


class JesusCreator(CharacterCreator):
    def create(self):
        return JesusClass()
