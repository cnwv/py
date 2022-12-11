with open('task_01.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        print(f'Строка {index} содержит {len(value.split())} слов')

