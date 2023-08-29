class Supermarket:
    def __init__(self, name, login, password, cnpj, shoppingItens=[]):
        self.name = name
        self.login = login
        self.password = password
        self.cnpj = cnpj
        self.shoppingItens = shoppingItens

    def validate_data(self):
        if not self.name:
            return 1

        if len(self.password) < 8 or not any(c.isupper() for c in self.password):
            return 2

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
            print("Senha deve ter 8 caracteres e conter pelo menos uma letra maiúscula")
            supermarket.password = input("Senha: ")
            print(supermarket.password)
    return supermarket
