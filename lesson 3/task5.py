def summa():
    s = 0
    while True:
        numb = input('Enter two number or press q for exit').split()
        for i in numb:
            if numb == 'q':
                return s
            else:
                try:
                    s += int(i)
                except ValueError:
                    print('To exit program press q')
        print(f'Sum of nunbers {s}')
print(summa())

