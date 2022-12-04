import sqlite3 as sq
from tkinter import *

with sq.connect('data.db') as db:
    cursor = db.cursor()
    print("Подключение к БД установлено!")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        class_num INTEGER DEFAULT 0,
        average_grade INTEGER DEFAULT 0,
        date_of_birthday INTEGER DEFAULT 0,
        phone_number INTEGER DEFAULT 0    
        )""")


temp_students = []
temp_class = []
name_id = []
temp_grage = []
temp_phone = []


def add_first_name():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (temp_students[0], temp_students[1], temp_students[2], temp_students[3], temp_students[4], temp_students[5], temp_students[6]))
    print('Данные в БД добавлены.')
    temp_students.clear()
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")


def get_all_student():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT rowid, * FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_first_name():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT first_name FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_second_name():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT second_name FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_last_name():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT last_name FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_class_num():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT class_num FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_average_grade():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT average_grade FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_date_of_birthday():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT date_of_birthday FROM students")
        all_data = cursor.fetchall()
    return all_data


def get_phone_number():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT phone_number FROM students")
        all_data = cursor.fetchall()
    return all_data


def del_all_student():
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")


# def change_class():
#     db = sq.connect('data.db')
#     print("Подключение к БД установлено!")
#     cursor = db.cursor()
#     cursor.execute(
#         f"UPDATE students SET class_num = ? WHERE rowid = {name_id[0]}", (temp_class))
#     print('Данные в БД добавлены.')
#     name_id.clear()
#     temp_class.clear()
#     db.commit()
#     db.close()
#     print("Подключение к БД закрыто!")

def change_class():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE students SET class_num = ? WHERE rowid = {name_id[0]}", (temp_students))
    print('Данные в БД добавлены.')
    name_id.clear()
    temp_students.clear()
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")


def change_average_grade():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE students SET average_grade = ? WHERE rowid = {name_id[0]}", (temp_grage))
    print('Данные в БД добавлены.')
    name_id.clear()
    temp_grage.clear()
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")


def change_phone():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE students SET phone_number = ? WHERE rowid = {name_id[0]}", (temp_phone))
    print('Данные в БД добавлены.')
    name_id.clear()
    temp_phone.clear()
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")


def del_student():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM students WHERE rowid = {name_id[0]}")
    print('Данные из БД удалены!!!.')
    name_id.clear()
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")
