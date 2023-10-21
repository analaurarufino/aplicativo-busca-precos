from modules.user.user import User
from modules.validation.validation import Validation


class Supermarket(User):
    def __init__(self, name, email, password, cnpj, products=[]):
        super().__init__(name, email, password)
        self.cnpj = cnpj
        self.products = products

    # Getter e setter adicionais para os atributos específicos da classe Supermarket
    def get_data(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "document": self.cnpj,
        }

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def products(self):
        return self.products

    def products(self, products):
        self.products = products

    def validate_data(self):
        Validation.validate_name(self.name)
        Validation.validate_email(self.email)
        Validation.validate_password(self.password)
        Validation.validate_cnpj(self.cnpj)
        return True
