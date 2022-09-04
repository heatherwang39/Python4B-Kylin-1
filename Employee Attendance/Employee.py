class Employee:
    def __init__(self, first_name, last_name, id, phone_number, address, present, absence):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.phone_number = phone_number
        self.address = address
        self.present = present
        self.absence = absence
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_id(self):
        return self.id
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    
    def get_present(self):
        return self.present
    
    def set_present(self, present):
        self.present = present
    
    def get_absence(self):
        return self.absence
    
    def set_absence(self, absence):
        self.absence = absence
