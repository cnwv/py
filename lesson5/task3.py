with open('task3.txt', 'r', encoding='utf-8') as f:
    my_line = f.read().split("\n")
    less = []
    average_salary = []
    for i in my_line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        average_salary.append(i[1])
print(f"Люди с зарплатой ниже 20000 - {less}. Средняя зп по палате - {sum(map(float, average_salary)) / len(average_salary)}")