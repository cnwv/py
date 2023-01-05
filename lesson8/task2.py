class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Div:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        try:
            if self.b == 0:
                raise OwnError('хуйня')
            else:
                return self.a / self.b
        except OwnError as err:
            print(err)


div = Div(11, 2)
print(div.division())
div_0 = Div(11, 0)
print(div_0.division())
