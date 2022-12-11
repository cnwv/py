import json
with open("task7.json", 'w', encoding='utf-8') as json_file:
    with open("task7.txt", 'r', encoding='utf-8') as file:
        firms = {}
        middle = {}
        s, n = 0, 0
        line = file.read().split("\n")
        for firma in line:
            firma = firma.split()
            profit = int(firma[2]) - int(firma[3])
            if profit > 0:
                firms[firma[0]] = profit

            if profit > 0:
                s += profit
                n += 1
            middle["middle profit"] = s / n
        all_list = [firms, middle]
        print(all_list)
    json.dump(all_list, json_file, indent=4)


