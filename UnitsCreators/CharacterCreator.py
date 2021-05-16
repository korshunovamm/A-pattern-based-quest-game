from abc import ABC, abstractmethod


class CharacterCreator(ABC):
    @abstractmethod
    def create(self):
        pass
