# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_num(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True


def list_prime_mult(n):

    if simple_num(n) == False:
        res = n
        for i in range(2, n):
            while res > 1:
                if res % i == 0:
                    res //= i
                    list.append(i)
                else:
                    break
            else:
                break
        print(f'Список простых множетелей числа: {n}')
        print(f'*'.join(map(str, list)))
    else:
        print('Простое число')


list = []

try:
    n = int(input('Введите натуральное число: '))
    list_prime_mult(n)
except:
    print('Введите натуральное число!')
