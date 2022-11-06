month = int(input("Вввод числа от 1 до 12\n: "))

my_dict = {1: "Зима", 2: "Зима", 12: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
           9: "Осень", 10: "Осень", 11: "Осень"}

autumm_monthes = [9, 10, 11]
winter_monthes = [12, 1, 2]
spring_monthes = [3, 4, 5]
summer_monthes = [6, 7, 8]

if month in autumm_monthes:
    print('autumm')
elif month in winter_monthes:
    print('winter')
elif month in spring_monthes:
    print('spring')
elif month in summer_monthes:
    print('summer')
else:
    print('error')

# print(my_dict.get(month))
