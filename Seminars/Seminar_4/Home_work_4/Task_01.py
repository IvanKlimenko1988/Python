# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.




n = int(input('Введите натуральное число: '))
res = []
if n > 0:
# Условия делимости
# 1-если число чётное, то делитель 2:
    prostoe = 2
    if n % 2 == 0:
        a = n
        count = 0
        while n > 1:
            if a % 2 == 0:
                a = a / prostoe
                res.append(int(a))
                n /= prostoe
                count += 1
            else:
                break
        print(res)
        print(count)
    else: 
        prostoe +=1
        print('Число нечётное')
else:
    print('Введите целое число N > 0')


# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10
# print(sum)
# if n / n == 1 and n / 1 == n:
#     print('простое')
# else:
#     print('нет')