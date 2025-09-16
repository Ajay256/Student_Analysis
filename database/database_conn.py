import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ajay1234#",
        database="student_analytics"
    )
    return conn

def fetch_performance_data():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT s.id, s.name, s.class, p.semester, sub.subject_name, p.marks, p.attendance
    FROM students s
    JOIN performance p ON s.id = p.student_id
    JOIN subjects sub ON p.subject_id = sub.id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data
