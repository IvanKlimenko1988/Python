# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# COUNT или FIND нельзя юзать! говорил же на семинаре.

str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')

str_3 = str_1.lower()
str_4 = str_2.lower()


print(str_3)
print(str_4)

# str_1 = 'Привет меня зовут Ваня'
# str_2 = 'Привет меня зовут Катя'
# print(str_1)
# print(str_2)
count = 0
list_1 = []
list_2 = []
lentgh = 0
while lentgh < len(str_4):
    if str_4 in str_3:
        count +=1
        lentgh +=1
    else:
        lentgh +=1
print(count)



