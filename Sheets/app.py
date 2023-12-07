import sqlite3
from openpyxl import Workbook
import os


if os.path.exists('projects.db'):
    os.remove('projects.db')
conn = sqlite3.connect('projects.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT,
        position TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        project_id INTEGER PRIMARY KEY,
        project_name TEXT,
        description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Working_process (
        process_id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        project_id INTEGER,
        FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
        FOREIGN KEY (project_id) REFERENCES Projects(project_id)
    )
''')

# Заполнение таблиц данными
cursor.executemany('INSERT INTO Employees (employee_id, name, position) VALUES (?, ?, ?)', [
    (1, 'Иван Иванов', 'Разработчик'),
    (2, 'Мария Петрова', 'Тестировщик'),
    (3, 'Алексей Сидоров', 'Дизайнер'),
])

cursor.executemany('INSERT INTO Projects (project_id, project_name, description) VALUES (?, ?, ?)', [
    (1, 'Проект А', 'Разработка нового продукта'),
    (2, 'Проект Б', 'Тестирование и оптимизация'),
])

cursor.executemany('INSERT INTO Working_process (process_id, employee_id, project_id) VALUES (?, ?, ?)', [
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 1),
    (4, 3, 2),
])

conn.commit()

workbook = Workbook()
sheet = workbook.active

sheet.append(['employee_id', 'name', 'position', 'project_id', 'project_name', 'description'])

cursor.execute('''
    SELECT Employees.employee_id, name, position, Projects.project_id, project_name, description
    FROM Employees
    JOIN Working_process ON Employees.employee_id = Working_process.employee_id
    JOIN Projects ON Working_process.project_id = Projects.project_id
''')

# Добавление данных в Excel
for row in cursor.fetchall():
    sheet.append(row)

workbook.save('company_data.xlsx')

conn.close()