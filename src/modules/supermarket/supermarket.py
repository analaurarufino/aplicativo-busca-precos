from modules.user.user import User

class Supermarket(User):
    def __init__(self, name, email, password, cnpj, shopping_items=[]):
        super().__init__(name, email, password)
        self.cnpj = cnpj
        self.shopping_items = shopping_items

    # Getter e setter adicionais para os atributos específicos da classe Supermarket
    def get_data(self):
        return {"name": self.name, "email": self.email, "password": self.password, "document": self.cnpj}

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

    def validate_data(self): #FUNÇÃO TEMPORÁRIA, IMPLEMENTAR VALIDAÇÃO
        return 0
    