from instance import Instances
from modules.validation.error import CustomError
from modules.controller.controller import (
    controllPOST,
    controllDELETE,
    controllCheckIsDataExists,
    controllGET,
    controllPUT,
    controllGETALL,
)


class SystemFacade:
    def __init__(self, input_fun, print_fun):
        self.instances = Instances(
            input_fun, print_fun
        )  # Inicia as instancias de todas classes

    def insert_buyer(self, user_data):
        res = controllPOST(
            user_data, self.instances.getDataPersistenceInstance(".Buyer")
        )
        if res == True:
            return "\nComprador inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Comprador\n"

    def insert_supermarket(self, user_data):
        res = controllPOST(
            user_data, self.instances.getDataPersistenceInstance(".Supermarket")
        )
        if res == True:
            return "\Supermercado inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Supermercado\n"

    def insert_product(self, product_data):
        res = controllPOST(
            product_data, self.instances.getDataPersistenceInstance(".Product")
        )
        if res == True:
            return "\Produto inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Produto\n"

    def get_all_product(self):
        res = controllGETALL(
            self.instances.getDataPersistenceInstance(".Product"),
        )
        return res

    def update_product(self, product_data, idTable):
        res = controllPUT(
            {"id": idTable},
            product_data,
            self.instances.getDataPersistenceInstance(".Product"),
        )
        if res == True:
            return "\nProduto atualizado com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Produto\n"

    def delete_product(self, idTable):
        res = controllDELETE(
            {"id": idTable},
            self.instances.getDataPersistenceInstance(".Product"),
        )
        if res == False:
            return "\nNão foi possivel excluir o Produto\n"
        else:
            return "\nProduto excluido com sucesso\n"

    def check_product_exists(self, idTable):
        res = controllCheckIsDataExists(
            idTable, self.instances.getDataPersistenceInstance(".Product")
        )
        return res

    def close(self):
        self.instances.close()
