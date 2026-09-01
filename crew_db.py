import sqlite3
connection=sqlite3.connect("crew.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS workers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT
)
""")
cursor.execute("DELETE FROM tasks")
cursor.execute("DELETE FROM workers")
connection.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT,
    hours REAL,
    worker_id INTEGER,
    FOREIGN KEY (worker_id) REFERENCES workers (id)
)
""")
connection.commit()
print("Tables created")
cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", ("Jake", "Electrician"))
cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", ("Maria", "Carpenter"))

connection.commit()

cursor.execute("INSERT INTO tasks (name, hours, worker_id) VALUES (?, ?, ?)", ("Install wiring", 8, 1))
cursor.execute("INSERT INTO tasks (name, hours, worker_id) VALUES (?, ?, ?)", ("Frame walls", 20, 2))

connection.commit()
print("Data inserted")
cursor.execute("""
    SELECT tasks.name, tasks.hours, workers.name, workers.role
    FROM tasks
    JOIN workers ON tasks.worker_id = workers.id
""")

results = cursor.fetchall()

print("Task assignments:")
for row in results:
    print(row)