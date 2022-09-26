a = int(input())
print(int(a % 10 + (a % 100 - a % 10)/10 + (a % 1000 - a % 100)/100))