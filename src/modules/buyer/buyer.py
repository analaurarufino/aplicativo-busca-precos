from user.user import User
from validation.validation import Validation

class Buyer(User):
    def __init__(self, name, email, password, user_id, favorite_supermarkets=[], shopping_list=[]):
        super().__init__(name, email, password, user_id)
        self.favorite_supermarkets = favorite_supermarkets
        self.shopping_list = shopping_list

    # Getter e setter adicionais para os atributos específicos da classe Buyer
    def get_favorite_supermarkets(self):
        return self.favorite_supermarkets

    def set_favorite_supermarkets(self, favorite_supermarkets):
        self.favorite_supermarkets = favorite_supermarkets

    def get_shopping_list(self):
        return self.shopping_list

    def set_shopping_list(self, shopping_list):
        self.shopping_list = shopping_list

class Buyer(User):
    def __init__(self, name, email, password, user_id, favorite_supermarkets=[], shopping_list=[]):
        super().__init__(name, email, password, user_id)
        self.favorite_supermarkets = favorite_supermarkets
        self.shopping_list = shopping_list


    def validate_data(self):
        if not Validation.validate_name(self.name):
            return 1

        if not Validation.validate_email(self.email):
            return 2

        if not Validation.validate_password(self.password):
            return 3

        return 0

    def print_informations(self):
        print(
            "{\n"
            "  name: ",
            self.name,
            "\n  email: ",
            self.email,
            "\n  password: ",
            self.password,
            "\n"
            "}\n",
        )


def addBuyer():
    name = input("Nome: ")
    email = input("Email: ")
    password = input("Senha: ")

    buyer = Buyer(name, email, password, [], [])

    while buyer.validate_data() != 0:
        if buyer.validate_data() == 1:
            print("Nome não pode ser vazio")
            buyer.name = input("Nome: ")
        elif buyer.validate_data() == 2:
            print("Email inválido")
            buyer.email = input("Email: ")
        elif buyer.validate_data() == 3:
            print(
                "Senha deve ter entre 8 e 20 caracteres e conter letras e números e ao menos 2 números"
            )
            buyer.password = input("Senha: ")

    return buyer
