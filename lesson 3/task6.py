def int_func(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result

print(int_func(input('Ввведи строку')))

