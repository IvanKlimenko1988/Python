# Задача FOOTBALL необязательная: Напишите программу, которая принимает на стандартный вход список игр 
# футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
import re



s_1 = 'Спартак;9;Зенит;10'.replace(';', ' ')
s_2 = 'Локомотив;12;Зенит;3'.replace(';', ' ')
s_3 = 'Спартак;8;Локомотив;15'.replace(';', ' ')
pattern = '\w+'
s1 = re.findall(pattern, s_1)
s2 = re.findall(pattern, s_2)
s3 = re.findall(pattern, s_3)
print(s1)
print(s2)
print(s3)
nums_1 = [int(i) for i in s1 if i.isdigit()]
nums_2 = [int(i) for i in s2 if i.isdigit()]
nums_3 = [int(i) for i in s3 if i.isdigit()]

def all_stat_match(array):
    if array[0] > array[1]:
        all_game_1 = 1
        all_game_2 = 1
        score_team_1 = 3
        score_team_2 = 0
        win_1 = 1
        win_2 = 0
        defeat_1 = 0 
        defeat_2 = 1 
        draw_1 = 0 
        draw_2 = 0 
    elif array[0] < array[1]:
        all_game_1 = 1
        all_game_2 = 1
        score_team_1 = 0
        score_team_2 = 3
        win_1 = 0
        win_2 = 1
        defeat_1 = 1
        defeat_2 = 0
        draw_1 = 0 
        draw_2 = 0 
    elif array[0] == array[1]:
        all_game_1 = 1
        all_game_2 = 1
        score_team_1 = 1
        score_team_2 = 1
        win_1 = 0
        win_2 = 0
        defeat_1 = 0 
        defeat_2 = 0
        draw_1 = 1
        draw_2 = 1
    return [[all_game_1, win_1, draw_1, defeat_1, score_team_1],[all_game_2, win_2, draw_2, defeat_2, score_team_2]]

stat_1 = all_stat_match(nums_1)
stat_2 = all_stat_match(nums_2)
stat_3 = all_stat_match(nums_3)
# print(stat_1)
# print(stat_2)


def add_team(text):
    teams = {}
    for i in text:
        if i.isdigit():
            continue
        elif i in teams:
                print("Taкая команда уже есть в базе")
        else:
            teams[i] = []
            print('Бренд успешно добавлен!')

            
    return teams

teams = add_team(s1)
teams = add_team(s2)
teams = add_team(s3)







# res_list = [x + y for x, y in zip(stat_1[1], stat_2[1])]

# print(res_list)

#


# teams[s1[0]] = stat_1[0]
# teams[s1[2]] = res_list



for key in teams.keys(): # Вывод всех ключей
                print(f'Команды: {key}')

for key in teams:
    print(f"{key}: {teams[key]}")






# elif command == "/all_brd":
#         print("Текущий список бредов машин:")
#         if len(brands_cars) == 0:
#             print("Список брендов пуст")
#         else:
#             for key in brands_cars.keys(): # Вывод всех ключей
#                 print(f'Бренд: {key}')
#     elif command == "/all_car":
#         car = brands_cars.get(input("Введите марку: "), 'Такой марки в базе нет!') #Проверка по ключу, если да, то выведен элемент
#         print(car)      
#     elif command == "/add_brd":
#         name = input('Введите бренд машины: ')
#         if name in brands_cars:
#                 print("Taкой бренд уже есть в базе")
#         else:
#             brands_cars[name] = []
#             print('Бренд успешно добавлен!')
#     elif command == "/add_car":
#         print("Выберете бренд, в который хотите модель машину: ")
#         name = input("Бренд: ")
#         if name in brands_cars:
#             car_name = input("Введите модель машины: ")
#             brands_cars[name] = [car_name]
#             print('Модель машины успено добавлена"!')     
#         else:
#             print("Ввелли несуществующий бренд!")