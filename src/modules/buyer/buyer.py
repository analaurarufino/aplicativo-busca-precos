class Buyer:
    def __init__(self, name, email, password, favoriteSupermarkets = [], shoppingList = []):
        self.name = name
        self.email = email
        self.password = password
        self.favoriteSupermarkets = favoriteSupermarkets
        self.shoppingList = shoppingList

    def validate_data(self):
        if not self.name:
            return 1 
        
        if "@" not in self.email or "." not in self.email:
            return 2 
        
        if len(self.password) < 8 or not any(c.isupper() for c in self.password):
            return 3 
        
        return 0

    def print_informations(self):
        print("{\n" "  name: ",self.name,"\n  email: ",self.email,"\n  password: ",self.password, "\n" "}\n")



def addBuyer():
    name = input("Nome: ")
    email = input("Email: ")
    password = input("Senha: ")

    buyer = Buyer(name, email, password, [], [])
    
    while(buyer.validate_data() != 0):
        if(buyer.validate_data() == 1):
            print("Nome não pode ser vazio")
            buyer.name = input("Nome: ")
        elif(buyer.validate_data() == 2):
            print("Email inválido")
            buyer.email = input("Email: ")
        elif(buyer.validate_data() == 3):
            print("Senha deve ter 8 caracteres e conter pelo menos uma letra maiúscula")
            buyer.password = input("Senha: ")
            print(buyer.password)
    return buyer