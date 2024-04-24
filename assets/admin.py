from sisfo.User import User
from student import Student
from professor import Professor
from superadmin import Superadmin

class Admin(User):
    def __init__(self, user_id, name, email, password,):
        super().__init__(user_id, name, email, password)
        self.admin_id = user_id
        
    def get_name(self):
        return self._name

    def create_user_account(self, user_type, *args):
        if user_type == "student":
            return Student(*args)
        elif user_type == "professor":
            return Professor(*args)
        elif user_type == "superadmin":
            return Superadmin(*args)
        else:
            return None
        
    def get_student_billing(self, student):
        if isinstance(student, Student):
            return student.calculate_billing()
        else:
            return "Error: Not a valid student object"
    
    def make_payment(self, user, amount):
        return f"Payment of Rp{amount} made successfully for {user.get_name()}."
    
    

