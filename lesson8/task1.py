class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transformation(cls, date):
        res = []
        for i in date.split("-"):
            res.append(int(i))
        return res

    @staticmethod
    def validate(date):
        day = date[0]
        month = date[1]
        year = date[2]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f"Date is correct"
                else:
                    return f"Year - {year} not correct"
            else:
                return f"Month - {month} not correct"
        else:
            return f"Day - {day} not correct"


print(Date.transformation("11-1111-1111"))
mc = Date.transformation("22-22-2222")
print(mc)
print(Date.validate([31, 11, 1111]))
print(Date.validate(mc))
