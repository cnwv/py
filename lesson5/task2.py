count = 0
#почему до цикла нужно все обозначать
with open("task_01.txt", "r", encoding="utf-8") as ass:
    for line in ass:
        count += 1
        line_word = line.split()
        print(line, "Кол-во слов ", len(line_word))
    print('Всего строк:', count)

