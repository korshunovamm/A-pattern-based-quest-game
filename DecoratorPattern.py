from abc import ABCMeta, abstractmethod


class IOperator(metaclass=ABCMeta):
    @abstractmethod
    def special_power(self):
        pass


class DoubleHulk(IOperator):

    def __init__(self, obj, number):
        self.obj = obj
        self.number = number
        self.obj.strength += 5 * self.number

    def special_power(self):
        # break the wall
        # decorator to call N-1 times
        print("You just broke the wall")
        print(self.obj)


class DoubleSherlockHolmes(IOperator):

    def __init__(self, obj, number):
        self.obj = obj
        self.number = number
        self.obj.intel += 5 * self.number

    def special_power(self):
        # get a hint
        # decorator to call N-1 times
        print("You just got a hint")
        print(self.obj)


class DoubleSpiderman(IOperator):

    def __init__(self, obj, number):
        self.obj = obj
        self.number = number
        self.obj.flex += 5 * self.number

    def special_power(self):
        # get sticked to ceiling
        # decorator to call N-1 times
        print("You just got sticked to ceiling")
        print(self.obj)


class DoubleJesus(IOperator):

    def __init__(self, obj, number):
        self.obj = obj
        self.number = number
        self.obj.health += 5 * self.number

    def special_power(self):
        # resurrect a character
        # decorator to call N times
        print("You just resurrected a character")
        print(self.obj)
