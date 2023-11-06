from modules.validation.validation import Validation
from modules.memento.memento import Memento

class Product:
    def __init__(self, name, price, subcategory):
        self.name = name
        self.price = price
        self.subcategory = subcategory

    def get_data(self):
        return {"name": self.name,  "price": self.price, "subcategory_id": self.subcategory,}


    def set_price(self, price):
        self.price = price

    def set_subcategory(self, subcategory):
        self.subcategory = subcategory

    def get_product_information(self):
        return f"Name: {self.name}, Price: {self.price}, Subcategory: {self.subcategory.get_name()}"
    
    def validate_data(self):
        Validation.validate_name(self.name)
        Validation.validate_price(int(self.price))
        # Supcategoria ainda não implementada
        # Validation.validate_subcategory(self.subcategory)
        return True

    def create_snapshot(self, id):
        return Memento(self, id)