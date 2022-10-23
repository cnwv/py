s = int(input('введи число'))
result = 0
while True:
    last_digit = s % 10
    if last_digit > result:
        result = last_digit
    s = s // 10
    if s == 0:
        break

print(result)





