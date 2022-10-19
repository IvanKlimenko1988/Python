# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
try:
    n = int(input('Введите целое число 1:'))
    m = int(input('Введите целое число 2:'))
except ValueError:
    n = int(input('Нужно ввести целое число 1:'))
    m = int(input('Нужно ввести целое число 2:'))

def nok(n, m):
    i = min(n, m)
    while True:
        if i % n == 0 and i % m == 0:
            break
        i += 1
    return(i)

def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


# def main():
#     try:
#         a = int(input('Input number A: '))
#         b = int(input('Input number B: '))
#     except ValueError as ex:
#         print('Input natural number!')
#         exit(ex)

#     print(f'LCM({a}, {b}) = {lcm(a, b)}')


# if __name__ == '__main__':
#     main()

