
class Printer:
    def __init__(self):
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


class Scanner:
    def __init__(self, scannerdict):
        self.scannerdict = scannerdict
        self.scanner_1 = 'HP ScanJet Pro 2000 s2'
        self.scanner_2 = 'Canon imageFORMULA DR-C225 II'
        self.scanner_3 = 'Mustek A3 F2400N'
        self.scannerdict = {}

    @property
    def scanner(self):
        self.scannerdict.setdefault(self.scanner_1)
        self.scannerdict.setdefault(self.scanner_2)
        self.scannerdict.setdefault(self.scanner_3)
        return self.scannerdict


class Xerox:
    def __init__(self, xeroxdict):
        self.xerox_1 = 'Xerox WorkCentre 3025BI'
        self.xerox_2 = 'Xerox B1032'
        self.xerox_3 = 'Xerox SS14'
        self.xeroxdict = xeroxdict


    @property
    def xerox(self):
        self.xeroxdict.setdefault(self.xerox_1)
        self.xeroxdict.setdefault(self.xerox_2)
        self.xeroxdict.setdefault(self.xerox_3)
        return self.xeroxdict


class WareHouse(Printer, Scanner, Xerox):
    def __init__(self):
        super().__init__(xeroxdict)

    def __str__(self):
        print(f"Cклад {self.name}")



moscow = WareHouse(Xerox(1))
moscow.xerox

# Menu
while True:
    print('Введите тип операции:\n  <1> Принять на склад\n  <2> Выдать со склада\n <3> Посмотреть наличие')
    action = input('>')
    if action == 3:
        print('Выберите товар: \n <1> Принтеры \n <2> Сканеры \n <3> Ксероксы')
        product = input('>')
        if product == 3:
            for i in moscow.xerox:
                print(i)
