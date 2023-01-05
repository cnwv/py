# TODO: переработать: сделать класс-исключение, переработать stop, переработать блок else
class MyList:
    def __init__(self, *args):
        self.my_list = []

    def add_list(self):
        while True:
            try:
                number = int(input("Вводи числа через Enter - "))
                self.my_list.append(number)
                print(f"Текущий список - \n {self.my_list}")
            except ValueError:
                print('Недопустимое значение')
                stop_word = input('Чтобы продолжить введи любой символ, для выхода введи - stop')
                if stop_word == 'stop':
                    return f"Выход из программы"
                else:
                    print(start_task.add_list())  # грубая ошибка


start_task = MyList(1)
print(start_task.add_list())
