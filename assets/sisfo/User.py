# base class
class User:
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id 
        self._name = name
        self._email = email
        self._password = password

    def login(self, email, password):  
        if email == self._email and password == self._password:
            return True
        else:
            return False

    def get_user_id(self): 
        return self._user_id
    
 