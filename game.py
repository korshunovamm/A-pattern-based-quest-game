from Units.ConcreateCreators import CreatorPersonality
from DecoratorPattern import DoubleHulk, DoubleSherlockHolmes

Character_client = CreatorPersonality('Hulk').create_character()
print(Character_client.health)
print(Character_client)


# groups

double_char = DoubleHulk(Character_client, 3)
# print(dir(double_char))
double_char.special_power()
print(double_char.obj.strength)

double_char1 = DoubleSherlockHolmes(CreatorPersonality('Hlms').create_character(), 2)
# print(dir(double_char))
double_char1.special_power()
print(double_char1.obj.intel)
