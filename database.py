import sqlite3

connection = sqlite3.connect("construction.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hours REAL,
        status TEXT
    )
""")
cursor.execute("DELETE FROM tasks")
connection.commit()
print("Table created successfully")
cursor.execute("INSERT INTO tasks (name, hours, status) VALUES (?, ?, ?)", ("Pour foundation", 12, "in progress"))
cursor.execute("INSERT INTO tasks (name, hours, status) VALUES (?, ?, ?)", ("Frame walls", 20, "not started"))
cursor.execute("INSERT INTO tasks (name, hours, status) VALUES (?, ?, ?)", ("Install wiring", 8, "complete"))

connection.commit()
print("Tasks inserted")
cursor.execute("SELECT * FROM tasks")
cursor.execute("SELECT * FROM tasks WHERE status = ?", ("complete",))
completed = cursor.fetchall()

print("Completed tasks:")
for row in completed:
    print(row)
rows = cursor.fetchall()
for row in rows:
    print(row)
