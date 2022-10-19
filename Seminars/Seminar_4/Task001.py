# t = (5,8,66)

# d=list(t)

# bd = {'test' : t}

# print(bd)

# bd['test'] = list(bd['test'] )

# print(bd)
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# fib = [0, 1]
# n = int(input(' Введите число: '))
# fibn = [0, 1]
# for i in range(2, n + 1):
#     next = fib[i-1] + fib[i-2]
#     if i % 2 == 0:
#         fibn.append(-next)
#     else:
#         fibn.append(next)
#     fib.append(next)
# print(fib)
# print(fibn)

# print(fibn[1:][::-1] + fib)

# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def check():
#     n = int(input('Введите целое число: '))
#     return n

# def make_list(n):
#     list_fib = [0,]
#     for i in range(1, n+1):
#         list_fib.append(fib(i))
#         list_fib.insert(0,(-1)**(i+1)*(fib(i)))
#         #list_fib.sort()
#     return list_fib

# print(fib(check()))
# print(make_list((check())))


def fibanachi(n):
    if n in (1, 2): 
        return 1
    else: 
        return fibanachi(n-1) + fibanachi(n-2)

N = int(input('Enter n: '))
fib_arr = []
for i in range(1, N + 1):
    fib_arr.append(fibanachi(i))
fib_arr.insert(0, 0)
for i in range(1, N + 1):
    fib_arr.insert(0, ((-1)**(i + 1)) * fibanachi(i))
print(fib_arr)



