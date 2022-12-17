import re

train_log = open(f"Train_Log.txt", mode="r")
form_log = open(f"Form_Log.txt", mode="w")

pattern = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w+) (\d+:\d+:\d+)"
for info in train_log:
    form_info = re.findall(pattern, info)
    print(f"{form_info}")
    form_log.write(f"{form_info}\n")