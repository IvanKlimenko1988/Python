# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа.
# Тема чат-бота любая. Просьба - постараться не использовать простой одномерный
# список или простой одномерный словарь.

from random import *
import json

def save():
    with open("brands.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(brands_cars, ensure_ascii=False))
    print("Коллекция марок машин успешно сохранена в файле brands.json")

def load():
    with open("brands.json", "r", encoding="utf-8") as fh:
        brands_cars = json.load(fh)
    return brands_cars

def print_2d_list(array):
    for i in range(len(array)):
        print(''.join(map(str, array[i])))

brands_cars = {}
models_cars = []

com_list = ["/menu - список всех комман", "/stop - завершение программы", "/all_brd - общмий список брендов", "/add_brd - добавить бренд",\
"/all_car - список моделей машин", "/add_car - Добавить модель машины", "/del - удалить бренд", "/save - сохранить изменения",\
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
    elif command == "/all_brd":
        print("Текущий список бредов машин:")
        if len(brands_cars) == 0:
            print("Список брендов пуст")
        else:
            for key in brands_cars.keys(): # Вывод всех ключей
                print(f'Бренд: {key}')
    elif command == "/all_car":
        car = brands_cars.get(input("Введите марку: "), 'Такой марки в базе нет!') #Проверка по ключу, если да, то выведен элемент
        print(car)      
    elif command == "/add_brd":
        name = input('Введите бренд машины: ')
        if name in brands_cars:
                print("Taкой бренд уже есть в базе")
        else:
            brands_cars[name] = []
            print('Бренд успешно добавлен!')
    elif command == "/add_car":
        print("Выберете бренд, в который хотите модель машину: ")
        name = input("Бренд: ")
        if name in brands_cars:
            car_name = input("Введите модель машины: ")
            brands_cars[name] = [car_name]
            print('Модель машины успено добавлена"!')     
        else:
            print("Ввелли несуществующий бренд!")
    elif command == "/del":
        print("Вы действительно хотите удалить бренд?")
        answer = input("Ведите да или нет:").lower()
        print(answer)
        if answer == "да":
            del_brd = input('Введите название бренда: ')
            if del_brd in brands_cars:
                del brands_cars[del_brd]
                print(f"Элемент с ключом {del_brd} удален")
        else:
            print("Такого бренда нет в базе!")
    elif command == "/save":
        save()
    elif command == "/load":
        brands_cars = load()
        print('Коллекция брендов успешно загружена!')     
    elif command == "/help":
        print_2d_list(com_list)
    else:
        print("Неопознная команда. Используйте справку /help")
