# my_fun = lambda p1, p2: p1 + p2
#
# print((lambda *args: args) (2, 5, 'sa'))
# def my_f():
#     global m_1, m_2
#     num1 = 67
#     num2 = 87
#     m_1 = num1 * num2 - number
#     m_2 = num1 ** num2
#     return m_1, m_2
#
# number = int(input("vvod chisla"))
# print(my_f())
# print(m_1)
# """def fun():
#     m1 = 5
#     def in_f():
#         nonlocal m1
#         m1 += 1
#         return m1
#     return in_f
# f = fun()
# print(f())
# """
p = input("Enter nubmers - ")
try:
    p = int(p)
    print(p)
except ValueError:
    print("Only numbers")

