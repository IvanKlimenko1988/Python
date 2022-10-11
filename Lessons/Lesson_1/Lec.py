# Типы данных и переменные
# int, float, boolean, str, list, None
# Python - язык с динамической типизацией


# value = None    # Переменная не инициализирована конкретным значением, но её можно инициализированить в другом месте
# a = 123
# b = 1.23
# value = 1233    # Здесь переменная изменила свой тип данных

# Для того чтобы узнать тип данных переменной:
# print(type(a))
# print(type(b))
# print(type(value))

# s = 'Hello world' # Использование последовательностей
# print(s)    # Вывод строки

# print(a, '-', b, '-', s) #Вывод нескольких переменных
# print('{} - {} - {}'.format(a, b, s)) #Форматированный вывод
# print(f'{a} - {b} - {s}') #Вывод с интерполяцией
# print('{1} - {2} - {0}'.format(a, b, s)) #Форматированный вывод с конкретным порядком

# f = True #Логическая переменная
# print(f)

# list = [1, 2, 3, 4]
# col = [1, 2, 3, 4, '1', '2', '3', True, 1.23] #В списке может быть разные типы данных
# print(list)
# print(col)


# Ввод и вывод данных
# print, input


# print('Введите а')
# a = int(input())   # Преобразование тива str в int
# print('Введите b')
# b = float(input()) # Преобразование тива str в float
# print(a, '+', b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# Арифметические операции
# +, -, *, /, %, //, **
# Сокращенные операции

# a = 1.3
# b = 3
# c = round(a * b, 3)
# print(c)

# a = 3
# a +=5
# print(a)


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции
# if, if - else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# user_name = input('Введите имя: ')
# if user_name == 'Маша':
#     print('Ура! это же Маша!')
# elif user_name == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif user_name == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', user_name)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)


# Управляющие конструкции
# for
# for i in 'qwerty':
#     print(i)

# Работа со строками

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))      #39 символов
# print('ешё' in text)  #True
# print(text.isdigit()) #False
# print(text.islower()) #True
# print(text.replace('ещё', 'ЕЩЁ')) #Замена подстроки в строке

# for c in text:
#     print(c)
# help(int) # подсказка о методе

# print(text[0]) #Вывод первого символа 'c'
# print(text[1]) #Вывод второго символа 'ъ'
# print(text[len(text)-1]) #Вывод последнего символа 'к'
# print(text[-5]) #Вывод 5-го символа с конца 'б'
# print(text[:]) #Вывод всего текста
# print(text[:2]) #Вывод от 0 до 2 индекса - 'съ'
# print(text[len(text)-2:]) # 'ok'
# print(text[6:-18]) # ещё этих мягких
# print(text[2:9]) # ешь ещё
# print(text[0:len(text):6]) # сеикакл - каждый 6-й симвл
# print(text[::6]) # сеикакл - каждый 6-й симвл
# text = text[2:9] + text[-5] + text[:2] # ешь ещёбсъ
# print(text)


# Списки: введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)              # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# numbers = list(ran)         
# print(numbers)              # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')# 5 len
# print(numbers)              # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *=2
#     print(i)                # [20, 4, 6, 8, 10]
# print(numbers)              # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)    # red greed blue

# for e in colors:
#     print(e*2)  # redred greengreen blueblue

# colors.append('gray') # Добавили в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # del colors[0] # удалить элемент


# Функции:

def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

