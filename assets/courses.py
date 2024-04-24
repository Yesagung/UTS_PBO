class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []
        self.grades = []
        

    def add_student(self, student):
        self.students_enrolled.append(student)

    def remove_student(self, student):
        if student in self.students_enrolled:
            self.students_enrolled.remove(student)
        else:
            print("Student not found in enrolled list.")
    
    def add_grade(self, grade):
        self.grades.append(grade)


    

