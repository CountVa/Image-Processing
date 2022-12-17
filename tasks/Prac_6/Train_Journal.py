
train_log = open(f"Train_Log.txt", mode="r")
form_log = open(f"Form_Log.txt", mode="w")
info = train_log.readline().rstrip('\n')
while info != '':
        if info.find('Рейс') != -1:
            info = info.split()
            form_info = f"[{info[6]}]: Поезд № {info[1]} {info[3]} {info[4]}"
            print(form_info)
            form_log.write(f"{form_info}\n")

        info = train_log.readline().rstrip('\n')