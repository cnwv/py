# калькулятор для проверки https://ru.onlinemschool.com/math/assistance/complex_number/calculation/
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b >= 0:  # если b отрицательное
            syntax = '+'
        else:
            syntax = '-'
        return f'{self.a + other.a}{syntax}{abs(self.b + other.b)}i'

    def __mul__(self, other):
        syntax = ''
        if self.a * other.b + self.b * other.a >= 0:
            syntax = '+'
        elif self.a * other.b + self.b * other.a < 0:
            syntax = '-'
        return f'{self.a * other.a - self.b * other.b}{syntax}{abs(self.a * other.b + self.b * other.a)}i'


z1 = ComplexNum(10, -5255)
z2 = ComplexNum(-15, -10)
z = z1 * z2
print(z)
print(z1+z2)