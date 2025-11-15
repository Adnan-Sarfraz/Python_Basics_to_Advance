def get_student_data():
    """Function to get student data: name and grades."""
    name = input("Enter student's name: ")
    grade = float(input(f"Enter grade for {name}: "))
    return name, grade

def calculate_grade(grade):
    """Function to calculate the grade letter based on score."""
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def student_grades_calculator():
    """Main function to drive the student grades calculation process."""
    num_students = int(input("Enter number of students: "))
    
    for _ in range(num_students):
        # Get student data
        name, grade = get_student_data()
        
        # Calculate grade letter
        grade_letter = calculate_grade(grade)
        
        # Display results
        print(f"{name}'s Grade: {grade_letter}")

# Call the main function to start the program
student_grades_calculator()
