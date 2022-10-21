# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа.
# Тема чат-бота любая. Просьба - постараться не использовать простой одномерный
# список или простой одномерный словарь.

from random import *
import json


def save():
    with open("brands.json", "w", encoding="utf-8") as ch:
        ch.write(json.dumps(brands, ensure_ascii=False))
    print("Коллекция марок машин успешно сохранена в файле brands.json")

def print_2d_list(array):
    for i in range(len(array)):
        print(''.join(map(str, array[i])))



brands = []
brands.append("BMW")
brands.append("Mersedes")
brands.append("Audi")
brands.append("KIA")
brands.append("Renaut")

com_list = ["/stop - завершение программы", "/all - общмий список брендов", "/add - добавить бренд",\
"/delete - удалить бренд", "/random - показать случайный бренд", "/save - сохранить изменения",\
"/load - загрузить коллекцию брендов"]

while True:
    command = input("Введите команду: ")
    if command == "/menu":
        print("Доступные команды:")
        print_2d_list(com_list)
    elif command == "/stop":
        save()
        print("Бот завершил свою роботу. Спасибо, рад был Вам помочь!")
        break
    elif command == "/all":
        print("Текущий список марок машин:")
        print(brands)
    elif command == "/add":
        new_car = input("Введите название марки: ")
        brands.append(new_car)
        print("Марка машины была успешно добавлена в коллекцию!")
    elif command == "/delete":
        del_car = input('Введите название марки: ')
        try:
            brands.remove(del_car)
            print("Марка успешно удалена!")
        except:
            print("Такой марки нет")
    elif command == "/random":
        print("Выбрана случайно марка: " + choice(brands))
    elif command == "/save":
        save()
    elif command == "/load":
        with open("brands.json", "r", encoding="utf-8") as cl:
            brands = json.load(cl)
        print('Коллекция машин успешно загружена!')     
    elif command == "/help":
        print("Cписок доступных комманд: /start, /stop, /all, /add")
    else:
        print("Неопознная команда. Используйте справку /help")
