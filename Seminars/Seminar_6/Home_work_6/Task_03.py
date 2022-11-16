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
s = 'Спартак;9;Зенит;10'.replace(';', ' ')
pattern = '\w+'
s1 = re.findall(pattern, s)

print(s1)
nums = [int(i) for i in s1 if i.isdigit()]

def find_match_score(array):
    if array[0] > array[1]:
        score_team_1 = 3
        score_team_2 = 0
    elif array[0] < array[1]:
        score_team_1 = 0
        score_team_2 = 3
    elif array[0] == array[1]:
        score_team_1 = 1
        score_team_2 = 1
    return [score_team_1, score_team_2]

print(find_match_score(nums))




