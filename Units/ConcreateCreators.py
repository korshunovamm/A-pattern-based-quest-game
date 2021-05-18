from Creators import Personality
from Products import HulkClass, SherlockHolmesClass, SpidermanClass, JesusClass


class CreatorPersonality(Personality):
    def factory(self):
        person_class = {
            "Hulk": HulkClass,
            "Hlms": SherlockHolmesClass,
            "Spider": SpidermanClass,
            "Jss": JesusClass
        }
        return person_class[self.name]()
