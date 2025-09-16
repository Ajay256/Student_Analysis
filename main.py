from Analysis import student_analysis, class_analysis, trend_analysis
from Visualization import charts
from Report import report_generator
from Alerts import student_alerts

def main_menu():
    while True:
        print("\n=== Student Performance Analytics System ===")
        print("1. Student Analysis")
        print("2. Class Analysis")
        print("3. Semester Trend Analysis")
        print("4. Visualizations")
        print("5. Generate Reports")
        print("6. Alerts for At-Risk Students")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            student_analysis.student_analysis()
        elif choice == '2':
            class_analysis.class_analysis()
        elif choice == '3':
            trend_analysis.trend_analysis()
        elif choice == '4':
            print("\nVisualization Options:")
            print("a. Student Performance Chart")
            print("b. Class Average Chart")
            print("c. Student Attendance Pie Chart")
            print("d. Performance vs Attendance Scatter Plot")
            vis_choice = input("Enter your choice (a-d): ")
            if vis_choice.lower() == 'a':
                student_name = input("Enter student name: ")
                charts.student_performance_chart(student_name)
            elif vis_choice.lower() == 'b':
                charts.class_average_chart()
            elif vis_choice.lower() == 'c':
                student_name = input("Enter student name: ")
                charts.attendance_pie_chart(student_name)
            elif vis_choice.lower() == 'd':
                charts.performance_vs_attendance()
            else:
                print("Invalid choice!")
        elif choice == '5':
            print("\nReport Options:")
            print("a. Student Report")
            print("b. Class Report")
            print("c. Semester Trend Report")
            report_choice = input("Enter your choice (a-c): ")
            if report_choice.lower() == 'a':
                student_name = input("Enter student name: ")
                report_generator.generate_student_report(student_name)
            elif report_choice.lower() == 'b':
                report_generator.generate_class_report()
            elif report_choice.lower() == 'c':
                report_generator.generate_semester_trend_report()
            else:
                print("Invalid choice!")
        elif choice == '6':
            student_alerts.generate_alerts()
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main_menu()
