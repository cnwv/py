my_list = [2, 4, 6]
new_list = [el+10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")


from sys import argv
script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print("Параметр 1: ", first_param)
print("Параметр 2: ", second_param)
print("Параметр 3: ", third_param)