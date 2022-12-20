from translate import Translator
translator = Translator(from_lang="ru", to_lang="en")
d = {}
d1 = {}
z = []
s = []
letter_log = open(f"dialog.txt", mode="r", encoding='utf-8')
gou_log = open(f"resul.txt", mode="w", encoding='utf-8')
info = letter_log.read().lower().replace("!", '').replace("?", '').replace(".", '').replace(",", '').replace("-",'').replace("\n", " ").split(" ")
for element in info:
    d[element] = info.count(element)
alphabet_sorted = dict(sorted(d.items()))
sorted_by_most = sorted(alphabet_sorted, key=alphabet_sorted.get, reverse=True)
for el in d:
    z.append(d.get(el))
z = sorted(z, reverse=True)
d1 = dict(zip(sorted_by_most, z))
translator = Translator(from_lang="ru", to_lang="en")
for goy in d1:
    s.append(translator.translate(goy))
for i in range(len(z)):
    gou_log.write("|")
    gou_log.write(str(z[i]))
    gou_log.write("|")
    gou_log.write(str(s[i]))
    gou_log.write("|")
    gou_log.write(str(sorted_by_most[i]))
    gou_log.write("|")
    gou_log.write("\n")
