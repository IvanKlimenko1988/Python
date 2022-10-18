# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from fractions import Fraction


def create_list(size):
    list = [0] * size
    for i in range(size):
        try:
            list[i] = float(input(f'Введите значение {i + 1}: '))
        except:
            print('Введите число')
    return list

list_1 = create_list(5)
print(list_1)




for i in range(len(list_1)):
    list_1[i] = list_1[i] - int(list_1[i])
    list_1[i] = Fraction.from_float(list_1[i])
  
    
min = list_1[0]    
max = list_1[0]    
for i in range(len(list_1)-1):
    if min > list_1[i + 1]:
        min = list_1[i + 1]
    else:
        max = list_1[i + 1]

print(list_1)
print()

print(min)
print(max)