from abc import ABC, abstractmethod


class AbsClass(ABC):
    def __init__(self, param=55):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Clothes(AbsClass):
    @property
    def consumption(self):
        return f'Общий расход ткани = {self.consumption_coat + self.consumption_suit}'


class Coat(Clothes):
    @property
    def consumption(self):
        Clothes.consumption_coat = round(self.param / 6.5 + 0.5)

        return


class Suit(Clothes):
    @property
    def consumption(self):
        return round(2 * self.param + 0.3)


prada = Clothes()
gucci = Suit(20)
tommy_hilfiger = Coat(24)
print(gucci.consumption)
print(tommy_hilfiger.consumption)
print(prada.consumption)
