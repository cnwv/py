def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return f'неверное условие задачи'
        else:
            res = 1
            for i in range(abs(y)):
                res *= 1 / x
            return f'x в степени y = {res}'
    except ValueError:
        return f'прога робит ток с числами'

x = input('Ввведи положительное число')
y = input('Введи целое отрицательное число')


print(my_func(x, y))