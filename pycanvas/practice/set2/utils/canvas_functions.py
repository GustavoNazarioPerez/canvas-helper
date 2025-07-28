# This class represents an Assignment in Canvas
class Assignment:
    def __init__(self, course: str, name: str, assignment_type: str, due_date: str):
        # These are instance variables — each Assignment has its own course, name, type, and due date
        self.course = course                    # e.g., "Physics II"
        self.name = name                        # e.g., "Newton's Laws"
        self.assignment_type = assignment_type  # e.g., "Quiz"
        self.due_date = due_date                # In YYYY-MM-DD format e.g., "2025-12-22"

    # Don't worry about this, but if you're curious...
    # this special method controls how the object appears when printed
    def __repr__(self):
        return f"{self.course} - {self.name} ({self.assignment_type}) due {self.due_date}"


def filter_by_class(assignments: list[Assignment], course_name: str) -> list[Assignment] | None:
    """
    Filters the list of assignments by course name.
    Example: filter_by_class(assignments, "Math") should return only Math assignments.
    """
    new_filtered = []
    for assignment in assignments:
        if assignment.course == course_name:
            new_filtered.append(assignment)
    return new_filtered
        

def sort_assignments(assignments: list[Assignment], order: str = "asc") -> list[Assignment] | None:
    
    """
    Sorts assignments by due date.
    If order == "asc", soonest due dates first.
    If order == "desc", latest due dates first.
    """
    if order=="asc":
        assignments.sort(key=get_date)
    elif order=="desc":
        assignments.sort(key=get_date, reverse=True)
    else:
        print("ERROR: YOU MUST SPECIFCY 'asc' or 'desc'. THIS LIST MAY BE SORTED")
    return assignments

# Feel free to use this anywhere to see what the assignments look like
def display_assignments(assignments: list[Assignment]):
    for a in assignments:
        print(a)
def get_date(assignment):
    return assignment.due_date