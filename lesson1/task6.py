a = int(input('Со скольких км стартуем?'))
b = int(input('Скок пробежать хочешь, если будем каждый день на 10% увеличивать?'))
d = 1
while True:
    if a <= b:
       a = a * 1.1
       d = d + 1
    if a >= b:
        break
print(d)
