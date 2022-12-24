class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Cell({self.amount}) - {"*" * self.amount}'

    def make_order(self, cell_in_row):
        row = ''
        for i in range(int(self.amount / cell_in_row)):
            row += ''.join('*' * cell_in_row) + '\n'
        row += f'{"*" * (self.amount % cell_in_row)}'
        return f'Cell({self.amount}) -  \n{row}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount * other.amount)
        else:
            return f'Not work, bro! Self cell less than other cell '

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount // other.amount)


k1 = Cell(15)
k2 = Cell(7)
s_12 = k1 / k2
print(s_12)
# print(k1.make_order(3))
print(s_12.make_order(2))

