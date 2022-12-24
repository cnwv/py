from abc import ABC, abstractmethod


class Absclass(ABC):
    def __init__(self, param=55):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Clothes(Absclass):

    @property
    def consumption_coat(self):
        pass

    @property
    def consumption_suit(self):
        pass

    @property
    def consumption(self):
        return f'Общий расход ткани = {self.consumption_coat + self.consumption_suit}'


class Coat(Clothes):
    @property
    def consumption(self):
        result = round(self.param / 6.5 + 0.5)
        Clothes.consumption_coat = result
        return f'Расход ткани на пальто {self.param} размера - {round(self.param / 6.5 + 0.5)}'


class Suit(Clothes):
    @property
    def consumption(self):
        result = round(2 * self.param + 0.3)
        Clothes.consumption_suit = result
        return f'Расход ткани на костюм {self.param} размера- {2 * self.param + 0.3}'


prada = Clothes()
gucci = Suit(20)
tommy_hilfiger = Coat(24)
print(gucci.consumption)
print(tommy_hilfiger.consumption)
print(prada.consumption)