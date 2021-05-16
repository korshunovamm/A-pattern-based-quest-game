from UnitsCreators.HulkCreator import HulkCreator
from UnitsCreators.SherlockHolmesCreator import SherlockHolmesCreator
from UnitsCreators.SpidermanCreator import SpidermanCreator
from UnitsCreators.JesusCreator import JesusCreator


class CreatorPersonality:
    def __init__(self, name):
        self.name = name

    def create_character(self):
        person_class = {
            "Hulk": HulkCreator(),
            "Hlms": SherlockHolmesCreator(),
            "Spider": SpidermanCreator(),
            "Jss": JesusCreator()
        }
        return person_class[self.name]

