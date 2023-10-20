from modules.validation.validation import Validation
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
    
    def validate_data(self):
        try:
            Validation.validate_name(self.name)
        except ValueError as e:
            print(f"Name validation error: {str(e)}")

        try:
            Validation.validate_price(self.price)
        except ValueError as e:
            print(f"Price validation error: {str(e)}")

        try:
           Validation.validate_subcategory(self.subcategory)
        except ValueError as e:
            print(f"subcategory validation error: {str(e)}")