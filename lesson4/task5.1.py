from functools import reduce
def my_list(el1, el2):
    return el1 * el2
un_list = [el for el in range(100, 1001, 2)]
print(reduce(my_list, un_list))

