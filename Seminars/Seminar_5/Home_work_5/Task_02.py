# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import re

def rle_compression(text):
    count = 1
    rle_str = ''
    i = 0
    while i < len(text):
        for j in range(len(text) - 1):
            if i >= len(text):
                break
            else:
                if text[i] == text[j + 1]:
                    count += 1
                    i += 1
                else:
                    rle_str += str(count) + text[i]
                    count = 1
                    i += 1
    return rle_str

def rle_recovery(text):
    res_str = ''
    num_filtr = re.compile('-?\d+')
    list_num = list(map(int, num_filtr.findall(text)))
    j = 0
    for i in range(len(text)):
        if not text[i].isdigit():
            res_str += str(text[i]) * list_num[j]
            j += 1
    return res_str

def load(file):
    with open(file) as data:
        start = data.read()
        print(f'Файл {file} успешно загружен.')
    return start

def save(file):
    with open('code.txt', 'w') as data:
        data.write(file)
        print('Файл успешно сохранён в "code.txt".')


start_string = load('start_file.txt')

code = rle_compression(start_string)
print(f'Входной файл сжат: {code}')
save(code)

de_code = rle_recovery(code)
print(f'Восстановление файла: {de_code}')

