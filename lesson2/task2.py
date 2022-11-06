my_list = input("Введите элементы списка: ").split()

for i in range(0, len(my_list) - 1, 2):
    a = my_list[i]
    b = my_list[i+1]
    my_list[i+1] = a
    my_list[i] = b

print(my_list)
# from ast import literal_eval
# l = input("Введите элементы списка: ").split()
# print(l)
# print(type(a))
# print(a)
# n = 0
# while True:
#     a = a[n:n + 1:2]
#     n = n + 1
#     if n == len(a):
#         break
# print(a)
#
