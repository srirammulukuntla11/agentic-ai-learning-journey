import sqlite3


connection = sqlite3.connect("students.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")


cursor.execute("DELETE FROM students")


students = [
    ("Rahul", "CSE"),
    ("Sriram", "AI/ML"),
    ("Priya", "ECE"),
    ("Anil", "AI/ML"),
    ("Kiran", "CSE")
]


cursor.executemany(
    "INSERT INTO students (name, course) VALUES (?, ?)",
    students
)


connection.commit()
connection.close()

print("Database created successfully!")
print("Student data inserted successfully!")