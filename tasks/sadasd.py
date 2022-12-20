def flatten_dict(d):
    new_dict = []
    keyz = [i for i in d.keys()]
    valuez = [i for i in d.values()]
    i = 0
    while len(new_dict) != len(keyz) + len(valuez):
       new_dict.append(keyz[i])
       new_dict.append(valuez[i])
       i += 1
    return new_dict
flatten_dict(3)