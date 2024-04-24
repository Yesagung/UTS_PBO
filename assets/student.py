from sisfo.User import User


class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.Enrollment_ID = enrollment_id
        self.Courses = []
        self.Grades = []
        self.Absences = {}
        self.viewpayment = []
        self.courses_enrolled = []
        
    
    def get_name(self):
        return self._name

    def Enroll_In_Course(self, course):
        self.courses_enrolled.append(course)
        print(f"{self.get_name()} has successfully enrolled in {course.name}.")

    def View_Course(self):
        if self.courses_enrolled:
            print("Courses Enrolled:")
            for course in self.courses_enrolled:
                print(f"{course.course_id} - {course.name}")
        else:
            print("No courses enrolled.")
        
    def View_Grade(self, course):
        grades = course.get_student_grades(self)
        self.Grades.extend(grades)  

    def record_attendance(self, student_name, date):
        print(f"Attendance recorded for {student_name} on {date}")

    def View_Schedule(self, course):
        schedule = course.get_schedule()
        print(schedule)

    def calculate_billing(self):
        total_billing = 10000000
        return total_billing
    
    def login(self, email, password):
        if email == self._email and password == self._password:
            return True
        else:
            return False

    def access_eticket(self, eticket, description):
        eticket.create_ticket(self.name, description)

    def create_ticket(self, description):
        print("students can create tickets that bugs occur!")
        print("Our team will look into it.")
        print("Ticket create succesfull.")
        print("Open Tickets:")
        print(f"User Name: {self._name}, Description: {description}")

    