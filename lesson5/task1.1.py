kaka = open("task_01.txt", "w", encoding='utf-8')
line = None
while line != '':
    line = input("Enter string for recording in file. Press ENTER for end.")
    kaka.write(f"{line}\n" if line != '' else kaka.close())