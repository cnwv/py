# my_list = [100, 200, 300, 100, 400]
# print(f"Srednee chislo - {sum(map(float, my_list)) / len(my_list)}")
# map what is it?
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task4_result.txt", "a") as result:
    with open("task4_source.txt", "r") as source:
        line = source.read().split("\n")
        for i in line:
            i = i.split(" - ")
            result.writelines(my_dict[i[0]] + " - " + i[1] + "\n")
