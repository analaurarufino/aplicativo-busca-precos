class Product:
    def __init__(self, name, price, subcategory):
        self.name = name
        self.price = price
        self.subcategory = subcategory

    def get_data(self):
        return {"name": self.name, "subcategory_id": self.subcategory, "price": self.price}


    def set_price(self, price):
        self.price = price

    def set_subcategory(self, subcategory):
        self.subcategory = subcategory

    def get_product_information(self):
        return f"Name: {self.name}, Price: {self.price}, Subcategory: {self.subcategory.get_name()}"
    
    def validate_data(self): # FUNÇÃO TEMPORÁRIA, IMPLEMENTAR VALIDAÇÃO
        return 0