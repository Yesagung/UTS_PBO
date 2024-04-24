class Grade:
    def __init__(self, student_id, course_id, numeric_score):
        self.Student_ID = student_id
        self.Course_ID = course_id
        self.Numeric_Score = numeric_score

    def Update_Grade(self, new_score):
        self.Numeric_Score = new_score
        print(f"Grade for Student {self.Student_ID} in Course {self.Course_ID} updated to {new_score}.")

