f_cool = open("text_4.txt", "r", encoding="utf-8")
for i in f_cool:
    print(i, end="")
# content = f_cool.readline()
# print(content)
# content = f_cool.readlines()
# print(content)
f_cool.close()