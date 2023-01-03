class Matrix:
    def __init__(self, num_array):
        self.num_array = num_array

    def __str__(self):
        matrix_str = ''
        for i in self.num_array:
            matrix_str += '  '.join(map(str, i)) + '\n'

        return matrix_str

    def __add__(self, other):
        result = []
        for i, x in zip(self.num_array, other.num_array):
            result.append(list(map(sum, zip(i, x))))
        return result


m = Matrix([[30, 3], [300, 3], [2, 5]])
c = Matrix([[30, 3], [3, 3], [276, 5]])
sum_matrix = m + c
print(sum_matrix)
