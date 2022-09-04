class Admin:
    def __init__(self, first_name, last_name, id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.password = password
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_id(self):
        return self.id
    
    def get_password(self):
        return self.password
