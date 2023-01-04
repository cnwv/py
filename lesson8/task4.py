class Printer:
    def __init__(self, model, amount, name):
        self.model = model
        self.amount = amount
        self.name = name


class Xerox:
    def __init__(self, model, amount, name):
        self.model = model
        self.amount = amount
        self.name = name


class Scanner:
    def __init__(self, model, amount, name):
        self.model = model
        self.amount = amount
        self.name = name


class WareHouse:
    def inventory(self):
        for x, i in enumerate(models):
            print(f"<{x}> {i.name} {i.model} - {i.amount} шт.")

    def add_goods(self, key, value):  # Получаем товар на склад
        models[key].amount += value

    def issue_goods(self, key, value): # Выдаем товар со склада
        models[key].amount -= value


models = [
    Printer('HP ScanJet Pro 200', 2, 'Принтер'),
    Scanner('HP LaserJet 400', 20, 'Сканер'),
    Xerox('Xerox WorkCentre 3025BI', 100, 'Ксерокс'),
    Xerox('Xerox WРВ 110', 0, 'Ксерокс'),
    Printer('HP MSk 123', 2, 'Принтер')
]
warehouse = WareHouse()
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
