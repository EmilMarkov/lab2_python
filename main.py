import os
from random import randint
from logging import log


print("Лабораторная работа №2. Для выхода из программы введите quit\n\n")


def generate(path):
    n = 100
    for i in range(n):
        size = randint(1, 100)
        with open(path + str(i + 1), "wb") as file:
            file.truncate(size * 1024)
            file.seek(size * 1024 - 1)
            file.write(b"\0")

# Основной цикл программы
while True:
    current_exercize = input("Введите номер задания: ") # номер задания

    # первое задание
    if (current_exercize == "1"):
        os.system("cls||clear") # очистка командной строки

        ipv6_file = "ipv6.log" # название файла с ipv6 файлом
        if (os.path.exists(os.getcwd() + rf"\{ipv6_file}")):
            os.remove(os.getcwd() + rf"\{ipv6_file}") # удаление файла при запуске программы
        log1 = log(ipv6_file) # log для первого упражнения

        for i in range(10000):
            ip = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(
                randint(0, 255)) # генерация ip
            log1.add(ip) # добавление сгенерированного ip в файл

        log1.print() # вывод сгенерированного файла

    # второе задание
    elif (current_exercize == "2"):
        os.system("cls||clear") # номер задания

        ipv6_file = "ipv6.log" # название файла с ipv6 файлом
        ipv4_file = "ipv4.log" # название файла с ipv6 файлом
        log2 = log(ipv6_file) # log для второго упражнения
        ipv6_count = 0
        ipv4_list = []
        ipv6_list = []

        if (os.path.exists(os.getcwd() + rf"\{ipv4_file}")):
            os.remove(os.getcwd() + rf"\{ipv4_file}")

        try:
            ipv6_count = sum(1 for line in open(os.getcwd() + rf"\{ipv6_file}")) # количество строк в файле ipv6
            ipv6_list = open(os.getcwd() + rf"\{ipv6_file}", "r").read().split('\n')[0:ipv6_count] # список ipv6
            ipv4_list = open(os.getcwd() + rf"\{ipv4_file}", "a") # список ipv4
        except Exception as ex:
            print(ex)
            continue

        for i in range(ipv6_count):
            ipv6_list[i] = ipv6_list[i].split('.')

        while True:
            checked = False
            mask = input("Введите маску сети: ").split('.')

            # обработка ошибки ввода маски
            if (len(mask) != 4):
                print("Mask format error!\n")
                continue
            else:
                for item in mask:
                    if (not (item.isdigit() and int(item) >= 0 and int(item) <= 255)):
                        print("Mask format error!\n")
                        continue
                    else:
                        checked = True

            if (checked):
                break

        for i in range(ipv6_count):
            ipv4 = ""
            for j in range(4):
                ipv4 += str(int(ipv6_list[i][j])&int(mask[j])) + "."
            ipv4_list.write(ipv4[:len(ipv4)-1] + '\n')

        ipv4_list.close()

    # третье задание
    elif (current_exercize == "3"):
        list_name = []
        sorted_list_2 = []

        with open("players.csv", 'r', encoding="utf-8") as players_base:
            flag = True
            for i in players_base:
                str_tm = i.replace('\n', "")
                str_tm = str_tm.split(';')
                if not flag:
                    name = (str_tm[0], int(str_tm[1]), int(str_tm[2]))
                    list_name.append(name)
                flag = False

        sorted_list = (sorted(list_name, key=lambda player: (player[1], player[2])))

        players_save = open("results.csv", 'w', encoding="utf-8")

        for i in range(len(sorted_list) - 1, 0, -1):
            save = str(sorted_list[i][0]) + ";" + str(sorted_list[i][1]) + ";" + str(sorted_list[i][2])
            players_save.write(str(save) + '\n')

    # четвёртое задание
    elif (current_exercize == "4"):
        path = "example\\"

        os.mkdir("example")

        generate(path)

    # пятое задание
    elif (current_exercize == "5"):
        tmp = input("Input 2 numbers: left/right\n")

        tmp_num = tmp.split("/")
        path = "example\\"
        left = int(tmp_num[0])
        right = int(tmp_num[1])

        count = 0

        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if left * 1024 <= os.path.getsize(f) and os.path.getsize(f) <= right * 1024:
                count += 1

        print("Number of files\t", count)

    # шестое задание
    elif (current_exercize == "6"):
        file_name = "article_rus.txt"
        text = open(os.getcwd() + r"\article_rus.txt", "r", encoding="utf-8").read() # файл с текстом
        letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0,
                   'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0,
                   'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0,
                   'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0,
                   'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0,
                   'э': 0, 'ю': 0, 'я': 0}


        text = ''.join(char for char in text if char.isalnum()).lower()

        for i in text:
            letters[i] += 1

        for i in letters.keys():
            letters[i] = int(letters[i] / len(text) * 100)

        print(letters)

    elif (current_exercize == "quit"):
        break

    else:
        os.system('cls||clear')
        print("Ошибка ввода!\n")
        os.system("pause")
