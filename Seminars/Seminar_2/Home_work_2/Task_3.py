# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# COUNT или FIND нельзя юзать! говорил же на семинаре.

def find_occurr(string1, string2):
    count = 0
    if string2 in string1:
        for i in range(len(string1)):
            if string1[i] == string2[0]:
                if string1[i:i + len(string2)] == string2:
                    count += 1
    print(f'Строка "{string2}" содержится в строке "{string1}" {count} раз')

try:
    string1 = input('Введите первую строку: ').lower()
    string2 = input('Введите вторую строку: ').lower()
    if len(string1) > len(string2):
        find_occurr(string1, string2)
    else:
        find_occurr(string2, string1)
except:
    print('Введите что-нибудь')


