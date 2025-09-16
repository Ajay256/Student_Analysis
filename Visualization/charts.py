import pandas as pd
import matplotlib.pyplot as plt
from database.database_conn import fetch_performance_data

# ----------------------------
# 1. Student Performance Chart
# ----------------------------
def student_performance_chart(student_name):
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])
    
    student_df = df[df['name'] == student_name]
    plt.figure(figsize=(8,5))
    plt.bar(student_df['subject'], student_df['marks'], color='skyblue')
    plt.title(f"{student_name} - Marks per Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.show()

# ----------------------------
# 2. Class Average Marks Chart
# ----------------------------
def class_average_chart():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])
    
    subject_avg = df.groupby('subject')['marks'].mean()
    plt.figure(figsize=(8,5))
    plt.bar(subject_avg.index, subject_avg.values, color='orange')
    plt.title("Class Average Marks per Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.show()

# ----------------------------
# 3. Attendance Pie Chart
# ----------------------------
def attendance_pie_chart(student_name):
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])
    
    student_df = df[df['name'] == student_name]
    attended = student_df['attendance'].sum()
    missed = len(student_df)*100 - attended
    
    plt.figure(figsize=(6,6))
    plt.pie([attended, missed], labels=['Attended','Missed'], autopct='%1.1f%%', colors=['green','red'])
    plt.title(f"{student_name} - Attendance")
    plt.show()

# ----------------------------
# 4. Performance vs Attendance Scatter
# ----------------------------
def performance_vs_attendance():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])
    
    plt.figure(figsize=(8,5))
    plt.scatter(df['attendance'], df['marks'], color='purple')
    plt.title("Performance vs Attendance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()
