from instance import Instances
from modules.validation.error import CustomError

class SystemFacade:
    def __init__(self, instances_instance=None):
        if instances_instance:
            self.instances = instances_instance
        else:
            input_fun = input
            print_fun = print
            self.instances = Instances(input_fun, print_fun)

    def insert_buyer(self, user_data):
        tableBuyer = self.instances.getDataPersistenceInstance('.Buyer')
        if tableBuyer:
            return self._insert_data(user_data, tableBuyer)
        return False

    def insert_supermarket(self, user_data):
        tableSupermarket = self.instances.getDataPersistenceInstance('.Supermarket')
        if tableSupermarket:
            return self._insert_data(user_data, tableSupermarket)
        return False

    def insert_product(self, product_data):
        tableProduct = self.instances.getDataPersistenceInstance('.Product')
        if tableProduct:
            return self._insert_data(product_data, tableProduct)
        return False

    def _insert_data(self, data, table):
        isValid = data.validate_data()
        if isValid == 0:
            try:
                table.insert(data.get_data())
                return True
            except:
                print(CustomError(message="Erro ao inserir na tabela"))
        else:
            print("\n", isValid, "\n")
        return False

    def close(self):
        self.instances.close()

