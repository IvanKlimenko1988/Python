# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def dec_to_bin(num):
    list = []
    while num > 0:
        res = num % 2
        list.append(res)
        num = num // 2
    for i in range(len(list)-1, -1, -1):
        list[i] = list[i]
        print(list[i], end='')


try:
    print('"\Перевод десятичного числа в двоичное/"')
    number = int(input('Введите целое число: '))
    print(f'Число {number} в двоичной форме: ')
    dec_to_bin(number)
except:
    print('Введите целое число!')
