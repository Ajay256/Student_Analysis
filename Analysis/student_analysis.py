import pandas as pd
from database.database_conn import fetch_performance_data

def student_analysis():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])

    # Average marks per student
    student_avg = df.groupby('name')['marks'].mean().sort_values(ascending=False)
    print("Average Marks per Student:")
    print(student_avg, "\n")

    # Identify strong & weak subjects for each student
    print("Strong & Weak Subjects per Student:")
    for student in df['name'].unique():
        student_data = df[df['name'] == student]
        strong_subject = student_data.loc[student_data['marks'].idxmax()]['subject']
        weak_subject = student_data.loc[student_data['marks'].idxmin()]['subject']
        print(f"{student} -> Strong: {strong_subject}, Weak: {weak_subject}")

    # Top 3 performers
    print("\nTop 3 Students:")
    print(student_avg.head(3))
