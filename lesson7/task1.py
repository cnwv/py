class Matrix:
    def __init__(self, num_array):
        self.num_array = num_array


    def __str__(self, c=''):
        self.c = c
        for i in self.num_array:
            self.c += '  '.join(map(str, i)) + '\n'

        return self.c
    def __add__(self, other, res=''):
        self.res = res
        for i, x in zip(self.num_array, other.num_array):
            summa = map(sum, zip(i, x))
            self.res += ' '.join(map(str, summa)) + '\n'
        return self.res


m = Matrix([[30, 3], [300, 3], [2, 5]])
c = Matrix([[30, 3], [3, 3], [276, 5]])
sum_matrix = m + c
print(sum_matrix)
