from sisfo.User import User

class Superadmin(User):
    def __init__(self, user_id, name, email, password, superadmin_id):
        super().__init__(user_id, name, email, password)
        self.superadmin_id = superadmin_id
    
    def get_name(self):
        return self._name

    def Provide_Technical_Support(self):
        print("Technical support provided")

    def Maintain_System(self):
        print("System maintenance performed")

    

        

    