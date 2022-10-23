a = int(input('ввод секунд '))
if a < 60:
    print(a, "Cекунд")
elif a >= 60 and a < 3600:
    c: int = a // 60 
    m = a % 60
    print(c, m)
elif a >= 3600:
    h = a // 3600
    m = (a - h * 3600) // 60
    c = a - h * 3600 - m * 60
    print(f'{h} час {m} минут {c} секунд')

