# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randint, random


k = int(input('Задайте степень: '))

list_ratio = []
while k > 0:
    list_ratio.append(randint(0, 1))
    list_ratio.append('x')
    list_ratio.append('^')
    list_ratio.append(k)
    list_ratio.append(' + ')
    k -= 1

list_ratio.append(randint(0, 100))
list_ratio.append(' = 0')
print(''.join(map(str, list_ratio)))