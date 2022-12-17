import random


# random(a)
def gois_2(total):
    a = [0, 1, 0]
    summa = 0
    for i in range(total):
        d = a.copy()
        b = random.randint(0, 2)
        if b == 0:
            d.pop(2)
        else:
            d.pop(0)
        if d[0] == 1:
            summa = summa + 1
    percent = summa / total * 100
    return (f"Процент выигрыша равен {percent}")