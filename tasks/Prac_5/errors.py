try:
    a = input('Введите имя файла:')
    text = open(f"{a}", mode="r")
    s = list()
    amount_check = 0
    amount = int(text.readline())
    for i in range(amount):
        c = text.readline().rstrip('\n')
        if c != '':
            amount_check += 1
            s.append(int(c))
        else:
            continue
    if amount_check != amount:
        raise Exception('Неверное количество элементов!')
    print(s)
except FileNotFoundError:
    print("Такого файла нет!")
except ValueError:
    print("Ошибка в значении параметра файла!")
else:
    text.close()