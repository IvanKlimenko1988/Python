# Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
# Вариант №1 Исходный текс переводи нижний регистр

# def del_words(text):
#     list_words = text.split()
#     i = 0
#     while i < (len(list_words)):
#         if 'абв' in list_words[i]:
#             list_words.pop(i)
#         else:
#             i +=1
#     return ' '.join(map(str, list_words))


# print('Привет, удалим все слова, содержащие "абв".')
# start_string = input('Введите текст: ').lower()
# res_str = del_words(start_string)
# print('Текст после удаления: ')
# print(res_str)

# Вариант № 2 Исходный текс не переводим весь в нижний регистр
# s = 'Привет, удалим все слова, содержащие "абв".'

def del_words(text):
    ch = 'абв'
    ch_1 = 'Абв'
    ch_2 = 'аБв'
    ch_3 = 'абВ'
    ch_4 = 'АБВ'
    ch_5 = 'АБв'
    ch_6 = 'аБВ'
    ch_7 = 'АбВ'
    list_words = text.split()
    i = 0
    while i < len(list_words):
        if ch in list_words[i] or ch_1 in list_words[i] or ch_2 in list_words[i] or ch_3 in list_words[i] or ch_4 in list_words[i] or ch_5 in list_words[i] or ch_6 in list_words[i] or ch_7 in list_words[i]:
            list_words.pop(i)
        else:
            i +=1
    return ' '.join(map(str, list_words))

print('Привет, удалим все слова, содержащие "абв".')
start_string = input('Введите текст: ')
res_str = del_words(start_string)
print('Текст после удаления: ')
print(res_str)


