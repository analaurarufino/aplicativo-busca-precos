from modules.user.user import User
from modules.validation.validation import Validation

class Buyer(User):
    def __init__(self, name, email, password, favorite_supermarkets=[], shopping_list=[]):
        super().__init__(name, email, password)
        self.favorite_supermarkets = favorite_supermarkets
        self.shopping_list = shopping_list

    # Getter e setter adicionais para os atributos específicos da classe Buyer
    def get_favorite_supermarkets(self):
        return self.favorite_supermarkets

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_favorite_supermarkets(self, favorite_supermarkets):
        self.favorite_supermarkets = favorite_supermarkets

    def get_shopping_list(self):
        return self.shopping_list

    def set_shopping_list(self, shopping_list):
        self.shopping_list = shopping_list
