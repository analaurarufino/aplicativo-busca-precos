from instance import Instances
from modules.api.supermarketApi import SupermarketAPIAdapter
from datetime import datetime
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class InsertBuyerCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, user_date):
        return self.system_facade.insert_buyer(user_date)
    
class InsertSupermarketCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self,user_data):
        return self.system_facade.insert_supermarket(user_data)

class InsertProductCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self,product_data):
        return self.system_facade.insert_product(product_data)

class GetAllProductCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self):
        return self.system_facade.get_all_product()

class UpdateProductCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, data):
        return self.system_facade.update_product(data["product_data"], data["idTable"])

class UpdateProductSupermarketCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade
     

    def execute(self, idTable):
        return self.system_facade.update_product_supermarket(idTable)

class DeleteProductCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, idTable):
        return self.system_facade.delete_product(idTable)

class CheckProductExistsCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, idTable):
        return self.system_facade.check_product_exists(idTable)

class LogUserActionCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, action):
        return self.system_facade.log_user_action(action)

class GetReportHtmlCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self):
        return self.system_facade.get_report_html()
class RestoreProduct(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self):
        return self.system_facade.undo_alter_product()

class CloseCommand(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self):
        self.system_facade.close()

class BackupDataProduct(Command):
    def __init__(self, system_facade):
        self.system_facade = system_facade

    def execute(self, item):
        return self.system_facade.backup_product(item["item"], item["id"])

# Defina outras classes de comando para outros métodos, como InsertSupermarketCommand, InsertProductCommand, etc.

class SystemFacade:
        
    def __init__(self, input_fun, print_fun):
        self.backup_prod = None
        self.instances = Instances(
            input_fun, print_fun
        )  # Inicia as instancias de todas classes
        self.system_facade = self
        self.instances = Instances(input_fun, print_fun)
        self.insert_buyer_command = InsertBuyerCommand(self.system_facade)
        self.insert_supermarket_command = InsertSupermarketCommand(self.system_facade)
        self.insert_product_command = InsertProductCommand(self.system_facade)
        self.get_all_product_command = GetAllProductCommand(self.system_facade)
        self.update_product_command = UpdateProductCommand(self.system_facade)
        self.update_product_supermarket_command = UpdateProductSupermarketCommand(self.system_facade)
        self.delete_product_command = DeleteProductCommand(self.system_facade)
        self.check_product_exists_command = CheckProductExistsCommand(self.system_facade)
        self.log_user_action_command = LogUserActionCommand(self.system_facade)
        self.get_report_html_command = GetReportHtmlCommand(self.system_facade)
        self.close_command = CloseCommand(self.system_facade)
        self.restore_product = RestoreProduct(self.system_facade)
        self.backup_data_product = BackupDataProduct(self.system_facade)

        self.commands = {
            "insert_buyer": self.insert_buyer_command,
            "insert_supermarket": self.insert_supermarket_command,
            "insert_product": self.insert_product_command,
            "get_all_product": self.get_all_product_command,
            "update_product": self.update_product_command,
            "update_product_supermarket": self.update_product_supermarket_command,
            "delete_product": self.delete_product_command,
            "check_product_exists": self.check_product_exists_command,
            "log_user_action": self.log_user_action_command,
            "get_report_html": self.get_report_html_command,
            "close": self.close_command,
            "restore_product": self.restore_product,
            "backup_product": self.backup_data_product,
        }

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name, data):
        # try:
            if command_name in self.commands:
                if data != '':
                    return self.commands[command_name].execute(data)
                else:
                    return self.commands[command_name].execute()
            else:
                return "Comando não encontrado."
        # except:
        #     return 'Ocorreu um erro ao executar o comando'
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

    def backup_product(self, product_data, id):
        self.backup_prod = product_data.create_snapshot(id)

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
        
    def undo_alter_product(self):
        if self.backup_prod == None:
            return '\nNão existe alterações feitas recentemente\n'
        else:
            id, item = self.backup_prod.restore()
            res = self.instances.controll.controllPUT(
                {"id": id},
                item,
                self.instances.getDataPersistenceInstance(".Product"),
            )
            self.backup_prod = None

            if res == True:
                return "\nAlterações desfeitas com sucesso\n"
            else:
                return "\nNão foi possivel reverter as alterações\n"

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
