with open('task_01.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введи строку для записи в файл')
        if not line:
            break


        print(line, file=f)