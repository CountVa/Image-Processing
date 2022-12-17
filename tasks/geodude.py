import degcalc
from random import randint


def rand_coord():
    a = randint(1 * 100000, 360 * 100000)
    return a / 100000


def spisok(*args, **kwargs):
    a = 0
    s = []
    for i in args:
        s.append(f"Point_{a} = {degcalc.deg_to_gms(i)}")
        a += 1
    for i, j in kwargs.items():
        s.append(f"{i} = {degcalc.deg_to_gms(j)}")
    return s


print(spisok(rand_coord(), rand_coord(), rand_coord(), les=rand_coord(), les_1=rand_coord()))