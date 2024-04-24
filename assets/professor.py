from sisfo.User import User

class Professor(User):
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.Faculty_ID = faculty_id
        self.Courses_Taught = []
        self.grade_list = {}
        self.monitoring_attendance = []
        self.update_schedule = []

    def get_name(self):
        return self._name

    def teach_course(self, course):
        self.Courses_Taught.append(course)
        
    def Upload_Grades(self, student_name, score):
        if score < 0 or score > 100:
            print("Error: Invalid score. Please provide a score between 0 and 100.")
            return
        self.grade_list[student_name] = score
        return self.grade_list

    def Monitor_Attendance(self, course):
        self.monitoring_attendance.append(course)

    def Update_Schedule(self, course):
        self.update_schedule.append(course)

    