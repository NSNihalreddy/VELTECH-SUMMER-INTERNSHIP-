from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Register Page
@app.route('/register')
def register():
    return render_template('register.html')


# Students Page
@app.route('/students')
def students():

    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return render_template(
        'students.html',
        students=students
    )


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Departments Page
@app.route('/departments')
def departments():
    return render_template('departments.html')


# Add Student
@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form['name']
    rollno = request.form['rollno']
    department = request.form['department']
    year = request.form['year']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    address = request.form['address']

    conn = get_db_connection()

    conn.execute(
        '''
        INSERT INTO students
        (
            name,
            rollno,
            department,
            year,
            email,
            phone,
            gender,
            address
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            name,
            rollno,
            department,
            year,
            email,
            phone,
            gender,
            address
        )
    )

    conn.commit()
    conn.close()

    return redirect('/students')


# Delete Student
@app.route('/delete_student/<int:id>')
def delete_student(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/students')


# Student Records Department Wise
@app.route('/student_records')
def student_records():

    conn = get_db_connection()

    cse = conn.execute(
        "SELECT * FROM students WHERE department='CSE'"
    ).fetchall()

    ece = conn.execute(
        "SELECT * FROM students WHERE department='ECE'"
    ).fetchall()

    eee = conn.execute(
        "SELECT * FROM students WHERE department='EEE'"
    ).fetchall()

    mechanical = conn.execute(
        "SELECT * FROM students WHERE department='Mechanical'"
    ).fetchall()

    civil = conn.execute(
        "SELECT * FROM students WHERE department='Civil'"
    ).fetchall()

    conn.close()

    return render_template(
        'student_records.html',
        cse=cse,
        ece=ece,
        eee=eee,
        mechanical=mechanical,
        civil=civil
    )


if __name__ == '__main__':
    app.run(debug=True)