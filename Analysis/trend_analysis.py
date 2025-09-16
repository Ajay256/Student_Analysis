import pandas as pd
from database.database_conn import fetch_performance_data
import matplotlib.pyplot as plt

def trend_analysis():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id', 'name', 'class', 'semester', 'subject', 'marks', 'attendance'])

    # Average marks per semester
    semester_avg = df.groupby('semester')['marks'].mean()
    print("Average Marks per Semester:")
    print(semester_avg)

    # Plot trend
    plt.plot(semester_avg.index, semester_avg.values, marker='o', linestyle='-', color='blue')
    plt.title("Class Average Marks Trend by Semester")
    plt.xlabel("Semester")
    plt.ylabel("Average Marks")
    plt.grid(True)
    plt.show()
