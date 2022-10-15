# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close() 

# with open('file.txt', 'a') as data:
#     data.write('line 123\n')
#     data.write('line 223\n')

# pach = 'file.txt'
# data = open(pach, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# import hello as h # Добавили скрипт и дали ему псевдоним (h)
# print(h.f(1)) # Выполнили функцию

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!')) #!!! Строка умножается на количество
# print(new_string(4)) # 12

# def concatenation(*params):
#     res: int = 0           # явное присвоение типа данных
#     for item in params:
#         res += item
#     return res

# print(concatenation('a','s','d','f')) #asdf - строка 
# print(concatenation('a','1')) #a1 - строка 
# print(concatenation(1,2,3,4,5)) # 15 - сумма целых чисел 

# def fib(n):
#     if n in [1, 2]: #условие выхода рекурсии
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for i in range(1, 10):
#     list.append(fib(i)) # Вызов рекурсии
# print(list)             #[1, 1, 2, 3, 5, 8, 13, 21, 34]

# a, b = 3, 4 # Множественное присваивание
# a = (3, 4) # Это уже кортеж!
# print(a)    #(3, 4)
# print(a[0]) # 3 - первый элемент кортежа
# print(a[-1]) # 4 - второй элемент кортежа
# b =(3, 5, 62, 32)
# print(b)
# print(b[2]) # 62

# t = tuple(['red', 'green', 'blue']) # Двойное преобразование - список в кортеж
# red, green, blue = t # множественное присваивание 
# print(type(red)) # Переменная хранит строку red
# print('r:{} g:{} b:{}'.format(red, green, blue))

# dictionary = {}
# dictionary = \
#     {
#         'up': '^',
#         'left': '<',
#         'down': 'v',
#         'right': '>'    
#     }                   # \ - чтобы не писать всё в одну строку
# print(dictionary)
# print(dictionary['up']) # Печать по ключу: ^

# for k in dictionary.values(): # элементы
#     print(k)

# del dictionary['up'] # удаление элемента по ключу
# print()
# for item in dictionary: # элементы
#     print('{}: {}'.format(item, dictionary[item])) # Вывод ключи: элементы

# colors = {'red', 'green', 'blue'} # Множество
# print(colors)   # {'red', 'greed', 'blue'}
# print(type(colors)) # set
# colors.add('gray') # Добавление элемента
# print(colors)   # {'green', 'red', 'blue', 'gray'}
# colors.remove('red')
# print(colors)   # {'green', 'blue', 'gray'}
# colors.discard('red') # если элемента нет, во множестве то удаление не вызовет ошибку
# colors.clear() # Очистка множества
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()    # Создали множество на основе множества 'a' 
# print(c)        # {1, 2, 3, 5, 8}
# u = a.union(b)  # Объединили множества
# print(u)        # {1, 2, 3, 5, 8, 13, 21} - повторяющихся элементов нет!
# i = a.intersection(b) # Пересечение двух множеств
# print(i)        # {8, 2, 5} - одинаковые элемента в 2-х множествах
# dl = a.difference(b) # Отличие множества а от b 
# print(dl)       # {1, 3}
# dl = b.difference(a) # # Отличие множества b от a 
# print(dl)       # {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)        # {1, 21, 3, 13}

# s = frozenset(a) # Множество нельзя изменять

list1 = [1, 2, 3, 4]
list2 = list1   # 1 2 3 4 

list1[0] = 123
list2[1] = 321
for e in list1:
    print(e, end= ' ')  # 123 321 3 4
print()
for e in list2:
    print(e, end= ' ')

list1.pop()  # Удление последнего элемента в списках
print(list1) # [123, 321, 3]
print(list2)
list1.pop(2) # Удаление элемента и индерсом 2
print(list1, list2) # [123, 321] [123, 321]
list1.append(555) # Добавление элемента в конец списка
print(list1)    # [123, 321, 555]
list1.insert(2, 111) # Добавление элемента 2 индекс
print(list1) #  [123, 321, 111, 555]