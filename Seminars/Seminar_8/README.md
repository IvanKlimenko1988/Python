# Простая информационная система - "Ученики" с базой данных SQLite3, реализованная на интерфейсе **tkinter**
---
### Условие задачи:
Создать информационную систему для работы с какой либо предметной областью.
ОБязательные требования:
1. разбиение на модули.
2. внешнее хранилище информации (или БД или файл формата txt / json / csv)
3. Функционал по просмотру, поиску, добавлению, редактированию, удалению информации.

Плюсами будет наличие ГУИ и/или наличие настоящей БД (SQLite3 / PostgreSQL)

1. требования - поиск и выдача информации,
2. добавление новой,
3. удаление,
4. внешнее хранилище данных,
5. разбиение на модули
---
## Разработчик: Клименко Иван
**Возможные операции:**
+ Вывод информации из БД(база данных)
+ Добавление информации в БД
+ Поиск информации в БД
+ Изменения данных в БД
+ Удаление информации из БД

---
Описание архитектуры:

+ **main** - точка входа в программу. Выполняет запуск программы.
+ **menu** - графический интерфейс стартовой страницы, где пользователь выбирает необходимую функцию программы.
+ **add_student** - модель для добавления полной информации об ученике.
+ **find_student** - модуль для вывода информации по фильтрам.
+ **сhange_info** - модуль для изменения данных ученика.
+ **del_student** - модуль для удаления ученика из базы данных. 
+ **bd_students** - модуль базы данных. Создаёт базу данных. В модуле реализованы простые запросы от пользователя.
+ **view** - модуль для создания графического интерфейса программы.
