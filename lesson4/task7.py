from itertools import count
from math import factorial
def factorial_fun():
    for i in count(1):
        yield factorial(i)
#почему так?

generator = factorial_fun()
x = 0
for n in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {n}")