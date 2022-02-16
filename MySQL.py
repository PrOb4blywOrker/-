import MySQLdb as mdb
import sqlite3
from tkinter import messagebox as mb

DBNAME="my_faculty"
DBHOST="localhost"
DBPASS=""
DBUSER="root"
##Показать БД в MySql(для messagebox)
def ShowMyDb(table):
    db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    postCur = db.cursor()
    postCur.execute(f"select * from {table}")
    rows = postCur.fetchall()
    db.close()
    return rows
#Экспорт из БД2 В БД3
def insertDb_my(table, column, value):
    db_lite = sqlite3.connect('faculty_lite.db')
    cur_lite = db_lite.cursor()
    cur_lite.execute(f"select SUBJECT, COURSE, TASK from {table} WHERE {column} = '{value}'")
    raws = cur_lite.fetchall()
    for data in raws:
        cur=db.cursor()
        cur.execute(f"INSERT INTO faculty_my (SUBJECT, COURSE, TASK) VALUES ('{data[0]}', '{data[1]}', '{data[2]}')")
        db.commit()
    mb.showinfo("Export from BD2 into BD3", f"{ShowMyDb('faculty_my')}")
try:
    db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("Database Connected Successfully")
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS faculty_my")
    cur.execute("""
            CREATE TABLE faculty_my(
            ID SERIAL PRIMARY KEY,
            SUBJECT TEXT,
            COURSE INT,
            TASK TEXT
            )
            """)
    print("Table created!")

except mdb.Error as e:
    print("Database Not Connected Successfully")
