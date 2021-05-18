from UnitsCreators.CharacterCreator import CharacterCreator
from Units.Hulk import HulkClass


class HulkCreator(CharacterCreator):
    def create(self):
        return HulkClass()
