import pandas as pd
import matplotlib.pyplot as plt
from database.database_conn import fetch_performance_data

# ----------------------------
# Export individual student report
# ----------------------------
def generate_student_report(student_name):
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id','name','class','semester','subject','marks','attendance'])
    
    student_df = df[df['name'] == student_name]
    
    # Export CSV
    csv_file = f"reports/{student_name.replace(' ','_')}_report.csv"
    student_df.to_csv(csv_file, index=False)
    print(f"CSV report generated: {csv_file}")
    
    # Export PDF (basic plot-based report)
    plt.figure(figsize=(8,5))
    plt.bar(student_df['subject'], student_df['marks'], color='skyblue')
    plt.title(f"{student_name} - Marks per Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.ylim(0,100)
    pdf_file = f"reports/{student_name.replace(' ','_')}_report.pdf"
    plt.savefig(pdf_file)
    plt.close()
    print(f"PDF report generated: {pdf_file}")

# ----------------------------
# Export class report
# ----------------------------
def generate_class_report():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id','name','class','semester','subject','marks','attendance'])
    
    subject_avg = df.groupby('subject')['marks'].mean().reset_index()
    
    # Export CSV
    csv_file = "reports/class_report.csv"
    subject_avg.to_csv(csv_file, index=False)
    print(f"CSV class report generated: {csv_file}")
    
    # Export PDF
    plt.figure(figsize=(8,5))
    plt.bar(subject_avg['subject'], subject_avg['marks'], color='orange')
    plt.title("Class Average Marks per Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0,100)
    pdf_file = "reports/class_report.pdf"
    plt.savefig(pdf_file)
    plt.close()
    print(f"PDF class report generated: {pdf_file}")

# ----------------------------
# Export semester trend report
# ----------------------------
def generate_semester_trend_report():
    data = fetch_performance_data()
    df = pd.DataFrame(data, columns=['student_id','name','class','semester','subject','marks','attendance'])
    
    semester_avg = df.groupby('semester')['marks'].mean().reset_index()
    
    # Export CSV
    csv_file = "reports/semester_trend.csv"
    semester_avg.to_csv(csv_file, index=False)
    print(f"CSV semester trend report generated: {csv_file}")
    
    # Export PDF
    plt.plot(semester_avg['semester'], semester_avg['marks'], marker='o', color='green')
    plt.title("Class Average Marks Trend by Semester")
    plt.xlabel("Semester")
    plt.ylabel("Average Marks")
    plt.grid(True)
    pdf_file = "reports/semester_trend.pdf"
    plt.savefig(pdf_file)
    plt.close()
    print(f"PDF semester trend report generated: {pdf_file}")
