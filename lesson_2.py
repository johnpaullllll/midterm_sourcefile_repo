import os

def classify_grade(grade):
 
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    
    students = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()

                if not cleaned_line or cleaned_line.startswith("#"):
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    continue

                student_id = parts[0].strip()
                name = parts[1].strip()

                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue

                if 0.0 <= grade <= 100.0:
                    students.append(
                        {
                            "student_id": student_id,
                            "name": name,
                            "grade": grade,
                        }
                    )
    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
    except OSError as e:
        print(f"Error accessing file '{file_path}': {e}")

    return students

def calculate_statistics(students):
    
    if not students:
        return None

    total_grade = 0.0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade

        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    count = len(students)
    average_grade = total_grade / count

    return {
        "count": count,
        "average": average_grade,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student,
    }


def display_students(students):
  
    if not students:
        print("No student records available to display.")
        return

    print("\n" + "=" * 65)
    print(
        f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}"
    )
    print("-" * 65)

    for student in students:
        classification, status = classify_grade(student["grade"])
        name_display = (
            student["name"][:18] + ".."
            if len(student["name"]) > 20
            else student["name"]
        )
        print(
            f"{student['student_id']:<12} {name_display:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}"
        )

    print("=" * 65)


def display_statistics(statistics):
  
    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['count']}")
    print(f"Class average:      {statistics['average']:.2f}")
    print(f"Passed:             {statistics['passed']}")
    print(f"Failed:             {statistics['failed']}")
    print(
        f"Highest:            {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}"
    )
    print(
        f"Lowest:             {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}"
    )


def search_student(students, keyword):
   
    cleaned_keyword = keyword.strip().lower()
    matches = []

    for student in students:
        if (
            cleaned_keyword in student["student_id"].lower()
            or cleaned_keyword in student["name"].lower()
        ):
            matches.append(student)

    return matches


def save_report(students, statistics, filename="grade_report.txt"):
  
    if not students or not statistics:
        print("No data available to write to report.")
        return

    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE REPORT\n")
            file.write("=" * 65 + "\n")
            file.write(
                f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}\n"
            )
            file.write("-" * 65 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(
                    f"{student['student_id']:<12} {student['name']:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}\n"
                )

            file.write("=" * 65 + "\n\n")
            file.write("CLASS SUMMARY\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total Students: {statistics['count']}\n")
            file.write(f"Class Average:  {statistics['average']:.2f}\n")
            file.write(f"Passed:         {statistics['passed']}\n")
            file.write(f"Failed:         {statistics['failed']}\n")
            file.write(
                f"Highest:        {statistics['highest']['name']} ({statistics['highest']['grade']:.2f})\n"
            )
            file.write(
                f"Lowest:         {statistics['lowest']['name']} ({statistics['lowest']['grade']:.2f})\n"
            )

        print(f"Report successfully saved to '{filename}'.")
    except OSError as e:
        print(f"Error saving report to '{filename}': {e}")


def main():
    
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded. Exiting program.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter search term (name or ID): ")
            matches = search_student(students, keyword)
            if matches:
                display_students(matches)
            else:
                print(f"No students found matching '{keyword}'.")
        elif choice == "4":
            save_report(students, statistics)
        elif choice == "5":
            print("Exiting Student Grade Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")
            continue


if __name__ == "__main__":
    main()