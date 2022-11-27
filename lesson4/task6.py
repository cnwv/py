from itertools import count, cycle
print('Program #1')
for i in count(int(input('Ввод стартового числа'))):
    print(i, end='') #как работает end
    quit =input()
    if quit == 'q':
        break
#почему так?
print('Program #2')
u_list =input('Введи список, разделяя элементы пробелом:').split()
iter = cycle(u_list)
quit = None

while quit!= 'q':
    print(next(iter), end= ' ')
    quit = input()