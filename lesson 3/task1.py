def fun_del(*args):
    try:
        n1 = int(input("Ввод делимого"))
        n2 = int(input("Ввод делителя"))
        delenie = n1 / n2
    except ValueError:
        return "Введи числа!!"
    except ZeroDivisionError:
        return "На ноль не делится!!!!"
    return delenie
print(f'Результат - {fun_del()}')
