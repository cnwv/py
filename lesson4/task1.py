from sys import argv
def zarplata():
    try:
        time, stavka, premia = map(int, argv[1:]) #почему [1:]?
        print(f'tvoya zarplata bydet - {time * stavka + premia}')
    except ValueError:
        print('Valuer Error')

zarplata()
