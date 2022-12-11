with open('task6.txt', "r", encoding='utf-8') as file:
    x = file.readlines()
    for s in x:
        str_1 = ''.join((i if i in '1234567890' else ' ') for i in s)
        str_2 = [int(i) for i in str_1.split()]
        print(f'{s.split()[0]} {sum(str_2)}')