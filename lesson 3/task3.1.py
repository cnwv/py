def myfunc(a, b, c):
    my_list = [a, b, c]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)
print(myfunc(2, 12, 4))

