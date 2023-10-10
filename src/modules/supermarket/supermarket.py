from user.user import User

class Supermarket(User):
    def __init__(self, name, email, login, password, cnpj, shopping_items=[]):
        super().__init__(name, email, password)
        self.cnpj = cnpj
        self.shopping_items = shopping_items

    # Getter e setter adicionais para os atributos específicos da classe Supermarket
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

    def get_shopping_items(self):
        return self.shopping_items

    def set_shopping_items(self, shopping_items):
        self.shopping_items = shopping_items


"""
    def validate_data(self):
        if not self.name:
            return 1

        if len(self.password) > 20 or len(self.password) < 8 or sum(c.isdigit() for c in self.password) < 2 or not any(c.isalpha() for c in self.password):
            return 2

        if len(self.login) > 12 or self.login == "" or any(char.isdigit() for char in self.login):
            return 3

        return 0

    def print_informations(self):
        print("{\n" "  name: ", self.name, "\n  Login: ", self.login,
              "\n  password: ", self.password, "\n" "}\n")


def addSupermarket():
    name = input("Nome: ")
    login = input("Login: ")
    password = input("Senha: ")
    cnpj = input("CNPJ: ")

    supermarket = Supermarket(name, login, password, cnpj, [])

    while (supermarket.validate_data() != 0):
        if (supermarket.validate_data() == 1):
            print("Nome não pode ser vazio")
            supermarket.name = input("Nome: ")
        elif (supermarket.validate_data() == 2):
            print(
                "Senha deve ter entre 8 e 20 caracteres e conter letras e números e ao menos 2 números.")
            supermarket.password = input("Senha: ")
            print(supermarket.password)
        elif (supermarket.validate_data() == 3):
            print("Login não pode conter números nem mais de 12 caracteres")
            supermarket.login = input("Login: ")
            print(supermarket.login)
    return supermarket
"""