import pandas as pd
from database.database_conn import fetch_performance_data

def class_analysis():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])

    # Average marks per subject
    subject_avg = df.groupby('subject')['marks'].mean()
    print("Average Marks per Subject:")
    print(subject_avg, "\n")

    # Pass/Fail percentage per subject (assuming pass >= 40)
    df['result'] = df['marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    pass_percent = df.groupby('subject')['result'].apply(lambda x: (x=='Pass').sum()/x.count()*100)
    print("Pass Percentage per Subject:")
    print(pass_percent, "\n")

    # Attendance statistics
    attendance_avg = df.groupby('subject')['attendance'].mean()
    print("Average Attendance per Subject:")
    print(attendance_avg)
