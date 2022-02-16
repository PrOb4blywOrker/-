from tkinter import *
from tkinter import messagebox as mb
import PostgreSQL
import MySQL
class Main:
    def __init__(self):
        self.MainWindow()

    def MainWindow(self):
        root.title('Главная страница')
        Button(root,text ="USER", width = 20, height = 3, command = self.UserWindow).grid(row=0, column=0)
        Button(root,text ="CRUD", width = 20, height = 3, command = self.CRUD).grid(row=1, column=0)


    def UserWindow(self):
        def searcbysubject():
            mb.showinfo("Поиск",f"Поиск за {self.Search.get()} \nРезультат поиска - {PostgreSQL.showFromDB_subj('faculty' , self.Search.get())}")

        def searchbyteacher():
            mb.showinfo("Поиск", f"Поиск за {self.Search.get()}\nРезультат поиска - {PostgreSQL.showFromDB_course('faculty' , self.Search.get())}")

        def searchbytask():mb.showinfo("Поиск", f"Поиск за {self.Search.get()}\nРезультат поиска - {PostgreSQL.showFromDB_task('faculty' , self.Search.get())}")

        userW = Toplevel(root)
        userW.title("USER")
        Label(userW,text="Поиск за :").grid(row=2,column=0)
        Button(userW,text="Предмет",width = 40, height = 3, command = searcbysubject).grid(row=3,column=0)
        Button(userW, text="Курс", width=40, height=3, command=searchbyteacher).grid(row=4, column=0)
        Button(userW, text="Задание(результат)", width=40, height=3, command=searchbytask).grid(row=5, column=0)
        Label(userW, text = "Значение для поиска:").grid(row=0,column=0)
        self.Search = Entry(userW,width=40)
        self.Search.grid(row=1,column=0)

    def CRUD(self):
        def UpdateBD():
            mb.showinfo("BD",f"{PostgreSQL.showDb('faculty')}")

        def ChangeBD():
            Change = Toplevel(root)
            Change.title("Change BD")
            Label(Change,text="Поменять значения в БД").grid(row=0,column=0)
            Label(Change, text="Таблица").grid(row=1, column=0)
            id=Entry(Change,width=40)
            id.grid(row=2,column=0)
            Label(Change, text="Старое значение").grid(row=3, column=0)

            oldV=Entry(Change,width=40)
            oldV.grid(row=4,column=0)
            Label(Change, text="Новое значение").grid(row=5, column=0)

            newV=Entry(Change,width=40)
            newV.grid(row=6,column=0)
            Label(Change, text="Изменяемая колонка").grid(row=7, column=0)

            ccg=Entry(Change,width=40)
            ccg.grid(row=8,column=0)
            Button(Change,text="Поменять",command=lambda:PostgreSQL.updateDb(id.get(),str(oldV.get()),str(newV.get()),ccg.get())).grid(row=9,column=0)

        def DeleteBD():
            Change=Toplevel(root)
            Change.title("Delete BD")
            Label(Change,text="Удалить значение в БД").grid(row=0,column=0)
            Label(Change,text="ID")
            id=Entry(Change,width=40)
            id.grid(row=2,column=0)
            Label(Change,text="Таблица").grid(row=3,column=0)
            table=Entry(Change,width=40)
            table.grid(row=4,column=0)
            Button(Change,text="Удалить",command=lambda:PostgreSQL.deleteFromDb(id.get(),table.get())).grid(row=7,column=0)


        def CreateBD():
            Change=Toplevel(root)
            Change.title("CreateBD")
            Label(Change,text="Создать запись").grid(row=0,column=0)
            Label(Change,text="Таблица").grid(row=1,column=0)
            table=Entry(Change,width=40)
            table.grid(row=2,column=0)
            Button(Change,text="Создать",command= lambda: PostgreSQL.createbd(table.get())).grid(row=7,column=0)

        def Export():
            Change=Toplevel(root)
            Change.title("Export")
            Label(Change,text="Export").grid(row=0,column=0)
            Label(Change,text="Таблица").grid(row=1,column=0)
            table = Entry(Change,width=40)
            table.grid(row=2,column=0)
            Label(Change,text="Поле в БД").grid(row=3,column=0)
            oldV=Entry(Change,width=40)
            oldV.grid(row=4,column=0)
            Label(Change,text="Значение поля БД").grid(row=5,column=0)
            newV=Entry(Change,width=40)
            newV.grid(row=6,column=0)
            Button(Change,text="Export",command=lambda:MySQL.insertDb_my(str(table.get()),str(oldV.get()),str(newV.get()))).grid(row=7,column=0)

        def Import():
            Change=Toplevel(root)
            Change.title("Import")
            Button(Change, text="Import",width=20,height=20, command=lambda: PostgreSQL.importdb()).grid(row=7,column=0)

        crud=Toplevel(root)
        crud.title("CRUD")
        Button(crud,text="Показать БД", width=20, height=3, command=UpdateBD).grid(row=1,column=0)
        Button(crud, text="Изменить БД", width=20, height=3, command=ChangeBD).grid(row=2, column=0)
        Button(crud, text="Создать БД", width=20, height=3, command=CreateBD).grid(row=0, column=0)
        Button(crud, text="Удалить запись з БД", width=20, height=3, command=DeleteBD).grid(row=3, column=0)
        Button(crud, text="Экспорт с БД2 в БД3", width=20, height=3, command=Export).grid(row=5, column=0)
        Button(crud, text="Импорт c БД1 в БД2", width=20, height=3, command=Import).grid(row=4, column=0)

if __name__ == "__main__":
    root = Tk()
    root.title("Главное меню")
    start = Main()
    root.mainloop()

