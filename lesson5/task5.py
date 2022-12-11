from random import randint
str_mf = " ".join([str(randint(1, 100)) for i in range(20)])
with open('task5.txt', mode='w+', encoding='utf-8') as file:
    file.write(str_mf)
    file.seek(0)
    print(sum(map(int, file.readline().split())))
    # чем рид от ридлайнс отличается
