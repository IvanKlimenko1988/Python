import sqlite3 as sq

# import add_student as st


    # ent_second_name = StringVar()
    # ent_name = StringVar()
    # ent_class = StringVar()
    # ent_grades = StringVar()
    # ent_birthday = StringVar()
    # ent_phone = StringVar()
with sq.connect('data.db') as db:
    cursor = db.cursor()
    print("Подключение к БД установлено!")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        first_name TEXT
        )""")

# student_id INTEGER PRIMARY KEY AUTOINCREMENT,
# last_name TEXT NOT NULL,    
#         second_name TEXT NOT NULL,
#         class INTEGER NOT NULL DEFAULT 1,
#         average_grade INTEGER NOT NULL DEFAULT 1,
#         date_of_birthday INTEGER NOT NULL DEFAULT 1,
#         phone_number INTEGER NOT NULL DEFAULT 1

def add_info(text):
    # cursor = db.cursor()
    cursor.execute("SELECT first_name FROM students")
    cursor.execute(f"INSERT INTO students VALUES ('{text}')")
    db.commit()
    print("Запись добавлена!")
    db.close()

# def create_db():
#     # Создание таблицы с полями 
#     print("Подключение к БД установлено!")
#     cursor.execute("""CREATE TABLE IF NOT EXISTS students (
#         first_name TEXT,
#         # name TEXT,
#         # second_name TEXT,
#         # class integer,
#         # average grade integer,
#         # date_of_birthday integer,
#         # phone_number integer
#     )""")
#     db.commit()
#     print('Усмпешное создание БД.')
#     db.close()
#     print("Подключение к БД закрыто!")



 
# db.commit()
# print('Усмпешное создание БД.')
# first_name = ''
# def add_first_name():
    
#     # cursor.execute(f"INSERT INTO students VALUES (?)", (first_name))
#     cursor.execute(f"INSERT INTO students VALUES ('{first_name}')")
#     db.commit()
#     db.close()
#     print("Подключение к БД закрыто!")




# def add_data():
#     cursor = db.cursor()
#     print("Подключение к БД установлено!")
# # Добавление данных
#     # cursor.execute(f"INSERT INTO students VALUES ('{st.ent_first_name}', '{st.ent_name}' , '{st.ent_second_name}', {st.ent_class}, {st.ent_grades}, {st.ent_birthday}, {st.ent_phone}')") 
#     # cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)", (st.ent_first_name, st.ent_second_name, st.ent_name, st.ent_class, st.ent_grades, st.ent_birthday, st.ent_phone)) 
#     cursor.execute(f"INSERT INTO students VALUES (?)", (first_name)) 
#     db.commit()
#     print('Данные в БД добавлены.')
#     db.close()
#     print("Подключение к БД закрыто!")

# # create_db()

# add_data()


# Выборка данных конкретно одного поля или несколько через запятую, если хотим все - ставим *, rowid - номер записи
# cursor.execute("SELECT rowid, * FROM students")
# print(cursor.fetchall()) #[(1, 'Ivanovich', 'Ivanov'), (2, 'Petrovich', 'Petrov')]
# print(cursor.fetchmany(1)) #Покажет одну запись в формате списка [(1, 'Ivanov', 'Ivan', 'Ivanovich', 5, 5, '23.03.2012', 75123523210)]
# print(cursor.fetchone()[1]) #Покажет одну запись в формате кортежа # Petrov

# Удаление данных
# cursor.execute("DELETE FROM students")
# cursor.execute("DROP TABLE IF EXISTS students")


