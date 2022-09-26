s = 0
i = 0
while i < 3:
    a = int(input())
    if a % 2 == 0:
        s = s + int(a / 2)
    else:
        s = s + int(a / 2) + 1
    i = i+1
print(s)