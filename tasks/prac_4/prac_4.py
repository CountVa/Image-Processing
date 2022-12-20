sd = []
g = open(f"data.txt", mode="r", encoding='utf-8')
s = open(f"data1.txt", mode="w", encoding='utf-8')
def read_line():
    z = g.read().split('\n')
    sd.append(z)
    sds = set(z)
    zsa = 0
    aaa = (sorted(sds))
    for i in range(len(sds)):
        zsa += 1
    print(f"Всего уникальных слов: {zsa} \n"
          f"============\n"
          f"{aaa}\n")
    s.write(f"Всего уникальных слов: {zsa}\n"
            f"===========\n"
            f"{aaa}\n")
read_line()