import random

a = random.randint(0, 50)
b = random.randint(0, 50)
lives = 3
right = 0
while lives != 0:
    print(f'{a} + {b}')

    answer = input(f"Введите сумму чисел от 0 до 100: ")
    if not answer.isdigit():
        print(f"Введите число")
        continue
    answer = int(answer)
    if answer > (a + b):
        print(f"Введенное число больше")
        lives -= 1
        print(f'Ваше количество жизней: {lives}')
    elif answer < (a + b):
        print("Введенное число меньше")
        lives -= 1
        print(f'Ваше количество жизней: {lives}')
    else:
        print(f'Вы угадали!')
        right += 1
        print(f'Количество правильных ответов: {right}')
        a = random.randint(0, 50)
        b = random.randint(0, 50)