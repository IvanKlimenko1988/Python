# Task003: Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
'''
def diap_digits(num):
    diap = []
    for i in range(-num,num + 1):
        diap.append(i)
    return diap

num = int(input("Введите число N: "))
res = diap_digits(num)
print(f'Диапазон чисел от {-num} да {num}: {res} ')
'''
try:
    n = int(input('Введите N: '))

    for i in range(-n, n + 1):
        print(i, end= ', ')
except:
    print('Введите число')