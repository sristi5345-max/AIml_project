from utils.calculator import GPACalculator
from utils.insights import InsightEngine
from utils.display import display_dashboard


def main():
    print("=" * 60)
    print("   Smart GPA Tracker & Grade Calculator with Insights")
    print("=" * 60)

    calculator = GPACalculator()
    insight_engine = InsightEngine()

    while True:
        print("\nMenu:")
        print("  1. Add Course")
        print("  2. View GPA & Dashboard")
        print("  3. Get ML Insights & Predictions")
        print("  4. Load Sample Data (Demo)")
        print("  5. Export Report")
        print("  6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            add_course(calculator)
        elif choice == "2":
            display_dashboard(calculator)
        elif choice == "3":
            get_insights(calculator, insight_engine)
        elif choice == "4":
            load_sample_data(calculator)
            print("✅ Sample data loaded!")
        elif choice == "5":
            export_report(calculator)
        elif choice == "6":
            print("\nGoodbye! 🎓")
            break
        else:
            print("Invalid choice.")


def add_course(calculator):
    name = input("Course name: ")
    credits = float(input("Credits: "))
    grade = input("Grade (A/B/etc or 0–100): ")
    semester = input("Semester: ")
    calculator.add_course(name, credits, grade, semester)


def get_insights(calculator, engine):
    if not calculator.courses:
        print("⚠️ No data.")
        return
    insights = engine.generate_insights(calculator)
    for i in insights:
        print("\n" + i)


def export_report(calculator):
    path = calculator.export_csv("outputs/report.csv")
    print(f"Saved to {path}")


def load_sample_data(calculator):
    sample = [
        ("Math", 4, "A", "Sem1"),
        ("Physics", 3, "B+", "Sem1"),
        ("DSA", 3, "A-", "Sem2"),
        ("DBMS", 3, "A", "Sem2"),
    ]
    for c in sample:
        calculator.add_course(*c)


if __name__ == "__main__":
    main()