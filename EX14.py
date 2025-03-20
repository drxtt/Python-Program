import sqlite3

# Database setup
DB_NAME = "students.db"

def create_table():
    """Create the Student table if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                student_course TEXT NOT NULL,
                student_email TEXT UNIQUE NOT NULL,
                student_dob DATE NOT NULL
            )
        """)
        conn.commit()

def add_student():
    """Add a new student."""
    try:
        name = input("Enter student name: ")
        course = input("Enter student course: ")
        email = input("Enter student email: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Student (student_name, student_course, student_email, student_dob)
                VALUES (?, ?, ?, ?)
            """, (name, course, email, dob))
            conn.commit()
            print("Student added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

def edit_student():
    """Edit details of a specific student."""
    student_id = input("Enter the student ID to edit: ")
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE student_id = ?", (student_id,))
            student = cursor.fetchone()
            if student:
                print("Current Details:", student)
                name = input(f"Enter new name ({student[1]}): ") or student[1]
                course = input(f"Enter new course ({student[2]}): ") or student[2]
                email = input(f"Enter new email ({student[3]}): ") or student[3]
                dob = input(f"Enter new DOB ({student[4]}): ") or student[4]
                
                cursor.execute("""
                    UPDATE Student
                    SET student_name = ?, student_course = ?, student_email = ?, student_dob = ?
                    WHERE student_id = ?
                """, (name, course, email, dob, student_id))
                conn.commit()
                print("Student details updated successfully!")
            else:
                print("Student not found.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def show_all_students():
    """Display details of all students."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student")
        students = cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

def show_one_student():
    """Display details of a specific student."""
    student_id = input("Enter the student ID to view: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if student:
            print("Student Details:", student)
        else:
            print("Student not found.")

def delete_student():
    """Delete a student record."""
    student_id = input("Enter the student ID to delete: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Student WHERE student_id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Student record deleted successfully!")
        else:
            print("Student not found.")

def main():
    create_table()  # Ensure the table exists
    while True:
        print("\nMenu:")
        print("1. Add a new Student")
        print("2. Edit a Student Detail")
        print("3. Show All Student Details")
        print("4. Show One Student Detail")
        print("5. Delete a Student Record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            edit_student()
        elif choice == '3':
            show_all_students()
        elif choice == '4':
            show_one_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
