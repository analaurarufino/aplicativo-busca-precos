from instance import Instances
from modules.api.supermarketApi import SupermarketAPIAdapter
from datetime import datetime


class SystemFacade:
    def __init__(self, input_fun, print_fun):
        self.instances = Instances(
            input_fun, print_fun
        )  # Inicia as instancias de todas classes
        

    def insert_buyer(self, user_data):
        res = self.instances.controll.controllPOST(
            user_data, self.instances.getDataPersistenceInstance(".Buyer")
        )
        if res == True:
            return "\nComprador inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Comprador\n"

    def insert_supermarket(self, user_data):
        res = self.instances.controll.controllPOST(
            user_data, self.instances.getDataPersistenceInstance(".Supermarket")
        )
        if res == True:
            return "\nSupermercado inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Supermercado\n"

    def insert_product(self, product_data):
        res = self.instances.controll.controllPOST(
            product_data, self.instances.getDataPersistenceInstance(".Product")
        )
        if res == True:
            return "\nProduto inserido com sucesso\n"
        else:
            return "\nNão foi possivel inserir o Produto\n"

    def get_all_product(self):
        res = self.instances.controll.controllGETALL(
            self.instances.getDataPersistenceInstance(".Product"),
        )
        return res

    def update_product(self, product_data, idTable):
        res = self.instances.controll.controllPUT(
            {"id": idTable},
            product_data,
            self.instances.getDataPersistenceInstance(".Product"),
        )
        if res == True:
            return "\nProduto atualizado com sucesso\n"
        else:
            return "\nNão foi possivel atualizar o Produto\n"
        

    #ATUALIZAR PRODUTOS POR APIs EXTERNAS 
    def update_product_supermarket(self, idTable):
        supermarket_api = SupermarketAPIAdapter("https://api.supermarket.com")

        # Obtém informações do produto da API externa
        product_info = supermarket_api.get_product_info(idTable)

        res = self.instances.controll.controllPUT(
            {"id": idTable},
            product_info,
            self.instances.getDataPersistenceInstance(".Product"),
        )
        if res == True:
            return "\nProduto atualizado com sucesso\n"
        else:
            return "\nNão foi possivel atualizar o Produto\n"

    def delete_product(self, idTable):
        res = self.instances.controll.controllDELETE(
            {"id": idTable},
            self.instances.getDataPersistenceInstance(".Product"),
        )
        if res == False:
            return "\nNão foi possivel excluir o Produto\n"
        else:
            return "\nProduto excluido com sucesso\n"

    def check_product_exists(self, idTable):
        res = self.instances.controll.controllCheckIsDataExists(
            idTable, self.instances.getDataPersistenceInstance(".Product")
        )
        return res

    def log_user_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        log_entry = f"{timestamp}: {action}\n"

        with open('logs.txt', 'a') as log_file:
            log_file.write(log_entry)

    def get_report_html(self):
        html = self.instances.getHtmlReportInstance()
        data = html.collect_data()
        dataHtml = html.format_report(data)
        html.save_report(dataHtml)
        return 'Relatorio salvo\n'

    def close(self):
        self.instances.close()
