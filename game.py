class Culture:
   """Культура"""
   def __repr__(self):
       return self.__str__()


class hulk(Culture):
   def makedict(self):
       self.char_dict = {'Intel': 1, 'Strength': 2, 'Flex': 3, 'Health': 4, 'Luck': 5}
   def __str__(self):
       return 'Hulk'


class doc(Culture):
   def __str__(self):
       return 'Doc'


class Character:
   def __init__(self, char_dict):
       self.intel = char_dict['intel']
       self.strength = char_dict['strength']
       self.flex = char_dict['flex']
       self.health = char_dict['health']
       self.luck = char_dict['luck']

   def __str__(self):
       return self.personality.__str__()

   def __repr__(self):
       return self.personality.__repr__()

   def make_char(self):
       """Задать строй правительству : это и есть наш Фабричный Метод"""
       raise AttributeError('Not Implemented Culture')


class Hulk(Character):
   def make_char(self):
       self.personality = hulk()


class Doc(Character):
   def make_char(self):
       self.personality = doc()


g1 = Hulk()
g1.make_char()
print(str(g1))
#
# g2 = Char2()
# g2.make_char()
# print(str(g2))

