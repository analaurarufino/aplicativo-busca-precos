class Category:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def get_subcategories(self):
        return self.subcategories

