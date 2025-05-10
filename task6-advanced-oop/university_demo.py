from instructor import Instructor
from student import Student
from course import Course
from teaching_assistant import TeachingAssistant

def main():
    try:
        print("\n=== University Simulation System ===")

        # Create instructor
        inst_name = input("Enter instructor name: ")
        inst_email = input("Enter instructor email: ")
        instructor = Instructor(inst_name, inst_email)

        # Create course
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        credits = int(input("Enter course credits (positive number): "))
        course = Course(course_code, course_name, credits)
        instructor.courses_taught.append(course)

        # Create students
        students = []
        num_students = int(input("How many students to add? "))
        for i in range(num_students):
            s_name = input(f"Enter name for student {i+1}: ")
            s_email = input(f"Enter email for student {i+1}: ")
            student = Student(s_name, s_email)
            students.append(student)

            enroll = input(f"Enroll {s_name} in {course_name}? (yes/no): ").strip().lower()
            if enroll == "yes":
                student.enroll(course)

        # Optionally, create a TA
        add_ta = input("Do you want to add a Teaching Assistant? (yes/no): ").strip().lower()
        if add_ta == "yes":
            ta_name = input("Enter TA name: ")
            ta_email = input("Enter TA email: ")
            ta = TeachingAssistant(ta_name, ta_email)
            ta.enroll(course)
            ta.courses_taught.append(course)
            students.append(ta)

        # Show course info
        print(f"\n--- {course} ---")
        print(f"Instructor: {instructor.name}")
        print("Enrolled Students:")
        for s in course:
            print(f"- {s}")

        # Show student enrollments
        print("\n--- Student Enrollments ---")
        for s in students:
            print(f"{s.name} is enrolled in:")
            for c in s:
                print(f"  • {c}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
