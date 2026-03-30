def display_dashboard(calc):
    if not calc.courses:
        print("No data")
        return

    print("\n===== DASHBOARD =====")
    for sem, courses in calc.courses_by_semester().items():
        print(f"\n{sem} GPA: {calc.semester_gpa(sem)}")
        for c in courses:
            print(f"{c.name} ({c.grade})")

    print("\nCumulative GPA:", calc.cumulative_gpa)