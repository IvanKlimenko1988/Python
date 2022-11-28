import sqlite3 as sq

from tkinter import *



with sq.connect('data.db') as db:
    cursor = db.cursor()
    print("Подключение к БД установлено!")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        first_name TEXT,
        second_name TEXT,
        last_name TEXT,
        class_num INTEGER,
        average_grade INTEGER,
        date_of_birthday INTEGER,
        phone_number INTEGER    
        )""")


temp_students = []

def add_first_name():
    db = sq.connect('data.db')
    print("Подключение к БД установлено!")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)", (temp_students[0], temp_students[1], temp_students[2], temp_students[3], temp_students[4], temp_students[5], temp_students[6]))
    print('Данные в БД добавлены.')
    db.commit()
    db.close()
    print("Подключение к БД закрыто!")

def get_all_student():
    all_data = []
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students")
        all_data = cursor.fetchall()
    return all_data

    
def del_all_student():
    with sq.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
    
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



# Удаление данных
# cursor.execute("DELETE FROM students")
# cursor.execute("DROP TABLE IF EXISTS students")


