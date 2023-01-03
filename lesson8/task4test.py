
class Printer:
    def __init__(self, printerdict):
        self.printerdict = printerdict
        self.printer_1 = 'HP HP LaserJet 400'
        self.printer_2 = 'CANON I-SENSYS LBP6030B PANTUM P2500W'
        self.printer_3 = 'EPSON L132'
        self.printerdict = {}

    @property
    def printer(self):
        self.printerdict.setdefault(self.printer_1)
        self.printerdict.setdefault(self.printer_2)
        self.printerdict.setdefault(self.printer_3)
        return self.printerdict




class WareHouse(Printer):
    def __init__(self):
        super().__init__(printerdict)

    def __str__(self):
        print(f"Cклад {self.name}")



moscow = Printer(1)


# Menu
while True:
    print('Введите тип операции:\n<1> Принять на склад\n<2> Выдать со склада\n<3> Посмотреть наличие')
    action = input('>')
    if action in ['1', '2', '3']:
        print('Выберите товар: \n<1> Принтеры\n<2> Сканеры\n<3> Ксероксы')
        product = input('>')
    if product == '1':
        for i in moscow.printer:
            s = 1
            print(f'<{s}>. {i} - {moscow.printer[i]} штук')
            s += 1

