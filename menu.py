from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import askstring
from db.postgres.connector import postgresDB

class DecanatMenu(tk.Tk): 
    def __init__(self):
        super().__init__()

        self.title("Decanat DataBase")
        self.geometry("500x500")
        self.button1 = ttk.Button(self, text="Відкрити таблицю #1", 
                                  command=self.open_table)
        self.button2 = ttk.Button(self, text="Відкрити таблицю #2")
        self.button3 = ttk.Button(self, text="Відкрити таблицю #3")
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def open_table(self):
        self.table = ttk.Treeview(self)
        self.table['columns']= ('id', 'course','group', 'student', 'subject')
        self.table.column("id", anchor=tk.CENTER, width=80)
        self.table.column("course", anchor=tk.CENTER, width=50)
        self.table.column("group", anchor=tk.CENTER, width=50)
        self.table.column("student", anchor=tk.CENTER, width=200)
        self.table.column("subject", anchor=tk.CENTER, width=200)

        self.table.heading("id",text="ID студента")
        self.table.heading("course",text="Курс")
        self.table.heading("group",text="Група")
        self.table.heading("student",text="Прізвище та ім'я студента")
        self.table.heading("subject",text="Дисципліна")

        records = postgresDB.read()
        for record in records:
            self.table.insert("", tk.END, values=record)
        
        self.but_create = tk.Button(text="Додати", command=self.add_student)
        self.but_create.pack()
        self.table.pack()

    def add_student(self):
        course = askstring('Курс', 'Введіть курс студента')
        group = askstring('Група', 'Введіть групу студента')
        name = askstring('Прізвище та ім\'я', 'Введіть ім\'я студента')
        subject = askstring('Дисципліна', 'Введіть дисципліну')
        data = [3, course, group, name, subject]
        postgresDB.create(data)
        print(data)
        self.table.insert("", tk.END, values=data)

if __name__ == "__main__":
    app = DecanatMenu()
    app.mainloop()