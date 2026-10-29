
class Student:
    def __init__(self, name, roll_no, marks_12th, cs1, cs2, cs3, acs1, acs2, acs3):
                 

        self.name = name
        self.roll_no = roll_no
        self.marks_12th = marks_12th

        self.cs1 = cs1
        self.cs2 = cs2
        self.cs3 = cs3

        self.acs1 = acs1
        self.acs2 = acs2
        self.acs3 = acs3

    # Task 1: Check whether 12th marks are below 60%
    def check_eligibility(self):
        x = self.marks_12th

        if x < 60:
            print("12th Marks are below 60%")
        else:
            print("12th Marks are 60% or above")

    # Task 2: Calculate average of CS subjects
    def average_marks(self):
        average = (self.cs1 + self.cs2 + self.cs3) / 3
        return average

    # Task 3: Calculate placement score
    def placement_score(self):
        x = self.average_marks()
        return x

    # Calculate average attendance
    def average_attendance(self):
        x = (self.acs1 + self.acs2 + self.acs3) / 3
        return x

    # Display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("12th Marks:", self.marks_12th, "%")

        self.check_eligibility()

        print("Average CS Marks:", self.average_marks())
        print("Placement Score:", self.placement_score())
        print("Average Attendance:", self.average_attendance(), "%")


# Create a student object
s1 = Student(
    "Rahul", 101, 75,
    80, 85, 90,
    90, 85, 95
)

s1.display()
