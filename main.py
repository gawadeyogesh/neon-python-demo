import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("PGHOST"),
    database=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD"),
    sslmode=os.getenv("PGSSLMODE")
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    marks INT NOT NULL
)
""")
conn.commit()


def insert_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    cur.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))
    conn.commit()
    print("✅ Student added successfully")


def view_students():
    cur.execute("SELECT * FROM students ORDER BY id")
    rows = cur.fetchall()
    print("\n--- Students List ---")
    for row in rows:
        print(row)


def update_student():
    sid = int(input("Enter student ID to update: "))
    new_marks = int(input("Enter new marks: "))
    cur.execute("UPDATE students SET marks=%s WHERE id=%s", (new_marks, sid))
    conn.commit()
    print("✏️ Student updated successfully")


def delete_student():
    sid = int(input("Enter student ID to delete: "))
    cur.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()
    print("🗑️ Student deleted successfully")


while True:
    print("\n===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        insert_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("❌ Invalid choice")

cur.close()
conn.close()
