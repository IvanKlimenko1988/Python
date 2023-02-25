# Задача
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые
# должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных
file_path = 'db.txt'
def getDB():
    with open(file_path, 'r', encoding="utf-8") as data:
        for line in data:
            print(line)

def add(person):
    with open(file_path, 'a', encoding="utf-8") as data:
        data.write('\n')
        data.write(person)
def find_person(person):
    with open(file_path, 'r', encoding="utf-8") as data:
        for line in data:
            if person in line:
                print(line)

def main():
    start = True
    while start:
        print('Простой "Телефонный справочник"')
        print("1.Контакты")
        print("2.Поиск")
        print("3.Добавить и сохранить")
        print("4.Вывести по фильтру")
        print("5.Выход")
        menuInput = int(input("Введите цифру меню: "))

        if menuInput == 1:
            print("База контактов: ")
            getDB()
        elif menuInput == 2:
            data = input("Введите данные: ")
            find_person(data)
        elif menuInput == 3:
            data = input("Введите данные (ФИО телефон): ")
            add(data)
        elif menuInput == 5:
            start = False
            print("Завершение программы!")



main()
