#  Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def create_point(size):
    point = [0] * size
    for i in range(size):
        try:
            point[i] = float(input(f"Введите координату {i+1}: "))
        except:
            print('Введите вещественное число')
    return point


def find_distance(first_point, second_point):
    sum = 0
    for i in range(len(first_point)):
        sum += (first_point[i] - second_point[i]) ** 2
    return sum ** 0.5


try:
    space_size = int(input('Введите размер пространства: '))
    print('Введите кординату точки A и В: ')

    point_a = create_point(space_size)
    point_b = create_point(space_size)
    res = find_distance(point_a, point_b)

    print(f'Расстояние в {space_size}D пространстве между точками А и В: {round(res, 2)}')
except:
    print('Введите число!')
