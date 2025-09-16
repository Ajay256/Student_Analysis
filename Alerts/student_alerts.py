import pandas as pd
from database.database_conn import fetch_performance_data

# Thresholds
LOW_MARKS_THRESHOLD = 40
LOW_ATTENDANCE_THRESHOLD = 75

def generate_alerts():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id','name','class','semester','subject','marks','attendance'])
    
    # Low marks alerts
    low_marks = df[df['marks'] < LOW_MARKS_THRESHOLD]
    if not low_marks.empty:
        print("Students with Low Marks (<40):")
        for index, row in low_marks.iterrows():
            print(f"{row['name']} | Subject: {row['subject']} | Marks: {row['marks']}")
    else:
        print("No students with low marks.")
    
    print("\n")
    
    # Low attendance alerts
    low_attendance = df[df['attendance'] < LOW_ATTENDANCE_THRESHOLD]
    if not low_attendance.empty:
        print("Students with Low Attendance (<75%):")
        for index, row in low_attendance.iterrows():
            print(f"{row['name']} | Subject: {row['subject']} | Attendance: {row['attendance']}%")
    else:
        print("No students with low attendance.")
    
    # Optional: Export alert report to CSV
    alerts_csv = "alerts/student_alerts.csv"
    combined_alerts = pd.concat([low_marks, low_attendance]).drop_duplicates()
    combined_alerts.to_csv(alerts_csv, index=False)
    print(f"\nAlert report exported: {alerts_csv}")
