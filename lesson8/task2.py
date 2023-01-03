class Div:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        try:
            return (self.a / self.b)
        except ZeroDivisionError:
            return f"Can't divide by null"


div = Div(11, 2)
print(div.division())
div_0 = Div(11, 0)
print(div_0.division())
