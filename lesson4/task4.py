from random import randint
my_list = [randint(1, 20) for i in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Сгенерированный список - {my_list} \n Список из удаленных повторяющиехся элементов - {new_list}')