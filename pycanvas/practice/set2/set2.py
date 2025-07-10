# This is going to cause some problems because the functions 'filter_by_class',
# 'sort_assignments', and 'display_assignments' haven't been imported from the
# 'canvas_functions' file in our 'utils' folder.
from utils.canvas_functions import Assignment

# 📋 Create some dummy Assignment objects to work with
assignments = [
    Assignment("Math", "Algebra Homework", "Homework", "2025-07-12"),
    Assignment("Science", "Lab Report", "Lab", "2025-07-10"),
    Assignment("Math", "Geometry Quiz", "Quiz", "2025-07-15"),
    Assignment("English", "Essay Draft", "Essay", "2025-07-08"),
    Assignment("Science", "Midterm", "Exam", "2025-07-18"),
]

# 🚀 Main program — this is where user interaction happens
def main():
    # Ask the user for which class they want to view assignments for
    course = 
    
    # Ask if they want assignments sorted from soonest or latest
    order = 

    # Use the functions to filter and sort the list
    filtered = filter_by_class(assignments, course)
    sorted_assignments = sort_assignments(filtered, order)
    
    # Show the results
    print(f"\nAssignments for {course}:")
    display_assignments(sorted_assignments)

# 🔁 Run the main program if this file is executed directly
if __name__ == "__main__":
    main()
