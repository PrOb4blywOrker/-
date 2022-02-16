from psycopg2 import connect
import psycopg2
import sqlite3
from tkinter import messagebox as mb

#Создание БД и записей в PostgreSQL
def createbd(table):
    conn = psycopg2.connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table}")
    cur.execute(f"""
            CREATE TABLE {table}(
            ID SERIAL PRIMARY KEY,
            SURNAME TEXT,
            NAME TEXT,
            PATRONYMIC TEXT,
            SUBJECT TEXT,
            COURSE INT,
            TASK TEXT
            )
            """)
    cur.execute(f"""
        INSERT INTO {table}(SURNAME, NAME, PATRONYMIC, SUBJECT, COURSE, TASK) VALUES 
        ('Ордынская','Зоя','Павловна','Высшая математика',1 , '2+2 (4)'),
        ('Новотарский','Михаил','Анатольевич', 'Python', 1 , 'print(2+2) (2+2)' ),
        ('Марковский','Александр','Петрович','Теория вероятности' , 2 , 'Объединение событий (AvB)'),
        ('Бойко','Ирина','Витальевна','Английский язык', 1 , 'Hello, (world!)'),
        ('Алещенко','Алексей','Вадимович','Java', 1 , 'System.out (.println())'),
        ('Виноградов','Юрий','Николаевич','Компьютерная электроника', 2 , 'P= (U*I)'),
        ('Иванов','Николай','Фёдорович','Основы SQL', 3 , 'Добавление в БД (INSERT INTO)'),
        ('Ребенчук','Татьяна','Львовна','Физика',1 , 'S= (U*t)'),
        ('Резников','Сергей','Анатольевич','Django',3 , 'Метод REST API для создания новой записи, которая добавляется в базу данных (POST)'),
        ('Шемсединов','Тимур','Гафарович','Технологии разработки Back-end',3 , 'Back-end - это (программно-аппаратная часть сервиса)')

        """)
    conn.commit()
#Поиск записей по предмету
def showFromDB_subj(table, value):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    postCur.execute(f"select * from public.{table} where subject = \'{value}\'");
    raws = postCur.fetchall()

    return raws
#Поиск записей по курсу
def showFromDB_course(table, value):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    postCur.execute(f"select * from public.{table} where course = \'{value}\'");
    raws = postCur.fetchall()

    return raws
#Поиск записей по заданиям(ответам)
def showFromDB_task(table, value):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    postCur.execute(f"select * from public.{table} where task = \'{value}\'");
    raws = postCur.fetchall()

    return raws

#Изменить запись в БД
def updateDb(table, oldVal, newVal, column):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    print(f"update {table} set {column} = {newVal} where {column} = {oldVal}")
    postCur.execute(f"update {table} set {column} = \'{newVal}\' where {column} = \'{oldVal}\'");
    pgConnect.commit()
    mb.showinfo("BD", f"{showDb('faculty')}")
#Показать БД
def showDb(table):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    postCur.execute(f"select * from {table}")
    rows = postCur.fetchall()
    pgConnect.close()
    return rows
#Показать БД в SqLite(для messagebox)
def showDBLITE(table):
    db = sqlite3.connect('faculty_lite.db')
    postCur = db.cursor()
    postCur.execute(f"select * from {table}")
    rows = postCur.fetchall()
    db.close()
    return rows

#Удалить запись с БД
def deleteFromDb(value, table):
    pgConnect = connect(database="alcnklnr", user="alcnklnr",
                        password="OiYfmteNFssTgtIhoi8PAkyPmpyHNkaA", host="castor.db.elephantsql.com", port="5432")
    postCur = pgConnect.cursor()
    print(f'delete from {table} where name = \'{value}\'')
    postCur.execute(f'delete from {table} where name = \'{value}\'')
    pgConnect.commit()
    mb.showinfo("BD", f"{showDb('faculty')}")

#Импорт из БД1 в БД2
def importdb():
    db = sqlite3.connect('faculty_lite.db')
    cur = db.cursor()

    cur.execute("""
                DROP TABLE faculty_lite
                """)


    cur.execute("""
            CREATE TABLE faculty_lite(
            ID SERIAL PRIMARY KEY NOT NULL ,
            SURNAME TEXT NOT NULL,
            NAME TEXT NOT NULL,
            PATRONYMIC TEXT NOT NULL,
            SUBJECT TEXT NOT NULL,
            COURSE INT NOT NULL,
            TASK TEXT NOT NULL
            )
            """)
    li=tuple(showDb())
    with db:
        cur=db.cursor()
        cur.executemany('INSERT INTO faculty_lite VALUES (?,?,?,?,?,?,?)', li)
    mb.showinfo("Import from BD1 into BD2", f"{showDBLITE('faculty_lite')}")
