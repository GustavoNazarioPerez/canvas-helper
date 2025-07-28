import unittest
from pycanvas.practice.set2.utils.canvas_functions import Assignment, filter_by_class, sort_assignments

# Create a few dummy assignments for testing
test_assignments = [
    Assignment("Math", "Homework 1", "Homework", "2025-07-10"),
    Assignment("Math", "Quiz 1", "Quiz", "2025-07-05"),
    Assignment("Science", "Lab Report", "Lab", "2025-07-12"),
    Assignment("English", "Essay", "Essay", "2025-07-08"),
]


class TestAssignmentUtils(unittest.TestCase):

    def test_filter_by_class(self):
        """Only returns assignments matching the course name."""
        result = filter_by_class(test_assignments, "Math")
        self.assertEqual(len(result), 2)
        for assignment in result:
            self.assertEqual(assignment.course, "Math")

    def test_sort_assignments_asc(self):
        """Sorts by soonest due date first."""
        sorted_list = sort_assignments(test_assignments, "asc")
        self.assertEqual(sorted_list[0].name, "Quiz 1")
        self.assertEqual(sorted_list[-1].name, "Lab Report")

    def test_sort_assignments_desc(self):
        """Sorts by latest due date first."""
        sorted_list = sort_assignments(test_assignments, "desc")
        self.assertEqual(sorted_list[0].name, "Lab Report")
        self.assertEqual(sorted_list[-1].name, "Quiz 1")


if __name__ == "__main__":
    unittest.main()
