from UnitsCreators.CharacterCreator import CharacterCreator
from Units.SherlockHolmes import SherlockHolmesClass


class SherlockHolmesCreator(CharacterCreator):
    def create(self):
        return SherlockHolmesClass()
