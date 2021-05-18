from Units.CreatorPersonality import CreatorPersonality
from DecoratorPattern import DoubleHulk, DoubleSherlockHolmes

Character_client = CreatorPersonality('Hulk').create_character()
character = Character_client.create()
print(character.health)
print(character)


# groups

double_char_hulk = DoubleHulk(character, 3)

double_char_hulk.special_power()
print(double_char_hulk.obj.strength)

double_char_hlms = DoubleSherlockHolmes(CreatorPersonality('Hlms').create_character().create(), 2)

double_char_hlms.special_power()
print(double_char_hlms.obj.intel)
