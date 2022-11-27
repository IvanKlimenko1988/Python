import sqlite3
import add_student as st


    # ent_first_name = StringVar()
    # ent_second_name = StringVar()
    # ent_name = StringVar()
    # ent_class = StringVar()
    # ent_grades = StringVar()
    # ent_birthday = StringVar()
    # ent_phone = StringVar()
db = sqlite3.connect('data.db')
cursor = db.cursor()

def create_db():
    # Создание таблицы с полями
    
    cursor.execute("""CREATE TABLE students (
        first_name text,
        name text,
        second_name text,
        class integer,
        average grade integer,
        date_of_birthday integer,
        phone_number integer
    )""")
    db.commit()
    db.close()

def add_data():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    print ()
# Добавление данных
    cursor.execute("INSERT INTO students VALUES (f {st.ent_first_name}, {ent_name} , {ent_second_name}, {ent_class}, {ent_grades}, {ent_birthday}, {ent_phone})")
# Выборка данных конкретно одного поля или несколько через запятую, если хотим все - ставим *, rowid - номер записи
# cursor.execute("SELECT rowid, * FROM students")
# print(cursor.fetchall()) #[(1, 'Ivanovich', 'Ivanov'), (2, 'Petrovich', 'Petrov')]
# print(cursor.fetchmany(1)) #Покажет одну запись в формате списка [(1, 'Ivanov', 'Ivan', 'Ivanovich', 5, 5, '23.03.2012', 75123523210)]
# print(cursor.fetchone()[1]) #Покажет одну запись в формате кортежа # Petrov

# Удаление данных
# cursor.execute("DELETE FROM students")


