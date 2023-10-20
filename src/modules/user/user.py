from modules.validation.validation import Validation
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Getters para os atributos
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_data(self):
        return {"name": self.name, "email": self.email, "password": self.password}

    # Setters para os atributos
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def validate_data(self):
        try:
            Validation.validate_name(self.name)
        except ValueError as e:
            print(f"Name validation error: {str(e)}")

        try:
            Validation.validate_email(self.email)
        except ValueError as e:
            print(f"Email validation error: {str(e)}")

        try:
           Validation.validate_password(self.password)
        except ValueError as e:
            print(f"Password validation error: {str(e)}")

        return 0

