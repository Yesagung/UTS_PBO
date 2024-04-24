class Attendance:
    def __init__(self, student_id, course_id, dates_absent):
        self.Student_ID = student_id
        self.Course_ID = course_id
        self.Dates_Absent = dates_absent

    def Record_Absence(self, date):
        self.Dates_Absent.append(date)
        print(f"Absence recorded for Student {self.Student_ID} in Course {self.Course_ID} on {date}.")

    def Calculate_Attendance_Rate(self, total_classes):
        total_absences = len(self.Dates_Absent)
        attendance_rate = ((total_classes - total_absences) / total_classes) * 100
        return attendance_rate
    


