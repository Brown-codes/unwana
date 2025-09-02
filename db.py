import sqlite3

DB_NAME = "app.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    matric TEXT UNIQUE NOT NULL
               ) """
)
conn.commit()
conn.close()
print("database initialized")


def add_student(name, matric):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO students (name, matric)
        VALUES (?, ?)""",
        (name, matric),
    )
    conn.commit()
    conn.close()
