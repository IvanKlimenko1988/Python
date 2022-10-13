# Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
try:
    print('Введите координату точки Х:', end=' ')
    coordinateX = int(input())
    print('Введите координату точки Y:', end=' ')
    coordinateY = int(input())
    if coordinateX > 0 and coordinateY > 0:
        print('Точка ннаходится в четверти: 1')
    elif coordinateX < 0 and coordinateY > 0:
        print('Точка ннаходится в четверти: 2')
    elif coordinateX < 0 and coordinateY < 0:
        print('Точка ннаходится в четверти: 3')
    elif coordinateX > 0 and coordinateY < 0:
        print('Точка ннаходится в четверти: 4')
    elif coordinateX == 0 and coordinateY == 0:
        print('Точка находится в центре осей координат')
    elif coordinateX == 0:
        print('Точка находится на оси Х')
    elif coordinateY == 0:
        print('Точка находится на оси Y')
except:
    print('Введите число!')
