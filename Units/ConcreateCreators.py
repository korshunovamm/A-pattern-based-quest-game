from Units.Characters import HulkClass, SherlockHolmesClass, SpidermanClass, JesusClass


class CreatorPersonality:
    def __init__(self, name):
        self.name = name

    def create_character(self):
        person_class = {
            "Hulk": HulkClass,
            "Hlms": SherlockHolmesClass,
            "Spider": SpidermanClass,
            "Jss": JesusClass
        }
        return person_class[self.name]()

