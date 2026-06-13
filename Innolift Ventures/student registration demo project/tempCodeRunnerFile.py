from flask import Flask, render_template, request
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

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

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
        (name, rollno, department, year,
         email, phone, gender, address)

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

    return '''
    <h2>Student Registered Successfully!</h2>
    <br>
    <a href="/students">View Students</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)