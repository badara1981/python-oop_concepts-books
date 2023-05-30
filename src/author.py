
class Author:
    def __init__(self, name:str, email:str, gender:str ='Male' or 'Female'):
        self.name = name
        self.email = email
        self.gender = gender
        
    def get_name(self):
        return self.name


    def get_email(self):
        return self.email
    
    def get_gender(self):
        return self.gender

    def set_email(self, email_required):
        
        self.email = email_required

    def __str__(self):
        return f"author[name={self.name}, email={self.email}, gender={self.gender}]"
 