#  TODO: переделать


# TODO: отсюда убраьт amount, переосмыслить name
class Orgtechnick:
    def __init__(self, model, amount, name):
        self.model = model
        self.amount = amount
        self.name = name


class Printer(Orgtechnick):
    pass


class Xerox(Orgtechnick):
    pass


class Scanner(Orgtechnick):
    pass


# TODO: переработать глобально: отказаться от MODELS(!!!) принимать в методах add экземпляры соответствующих классов
class WareHouse:
    MODELS = [
        Printer('HP ScanJet Pro 200', 2, 'Принтер'),
        Scanner('HP LaserJet 400', 20, 'Сканер'),
        Xerox('Xerox WorkCentre 3025BI', 100, 'Ксерокс'),
        Xerox('Xerox WРВ 110', 0, 'Ксерокс'),
        Printer('HP MSk 123', 2, 'Принтер')
    ]

    def __init__(self):
        self.storage = {}

    def inventory(self):
        for x, i in enumerate(self.MODELS):
            print(f"<{x}> {i.name} {i.model} - {i.amount} шт.")

    # TODO: принимать объекты классов!!!!
    # def add_goods(self, object, amount)
    def add_goods(self, key, value):  # Получаем товар на склад
        self.MODELS[key].amount += value
        # self.storge[key].append(object)

    def issue_goods(self, key, value): # Выдаем товар со склада
        self.MODELS[key].amount -= value


if __name__ == "__main__":

    warehouse = WareHouse()

    # some_printer = Printer()
    # warehouse.add_goods(some_printer)

    # Menu
    while True:
        print(f'Выберете действие: \n<1> Получение товара\n<2> Отгрузка товара')
        action = input('> ')
        if action in ['1', '2']:
            print('Выберите продукт:')
            warehouse.inventory()
        product = int(input('>'))
        print('Выбери количество - ')
        try:
            add_rem = int(input('кол-во > '))
        except ValueError:
            print('Неверный тип данных')

        if action == '1':
            warehouse.add_goods(product, add_rem)

        elif action == '2':
            warehouse.issue_goods(product, add_rem)
