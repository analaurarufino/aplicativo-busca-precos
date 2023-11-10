from modules.validation.error import ErrorBuilder

#Padrão Decorator
class ControllerInterface:
    def controllPOST(self, data, table):
        pass

    def controllGET(self, conditions, table):
        pass

    def controllGETALL(self, table):
        pass

    def controllPUT(self, conditions, data, table):
        pass

    def controllDELETE(self, conditions, table):
        pass

    def controllCheckIsDataExists(self, idTable, table):
        pass

class ConcreteController(ControllerInterface):
    def controllPOST(self, data, table):
        try:
            data.validate_data()
            table.insert(data.get_data())
            return True
        except Exception as e:
            error_instance = ErrorBuilder(f"Erro ao inserir dados na tabela: ").add_code(409).add_details(str(e)).build()
            print('\n', error_instance)
            return False

    def controllGET(self, conditions, table):
        try:
            return table.get(conditions)
        except Exception as e:
            error_instance = ErrorBuilder(f"Erro ao buscar dados na tabela: ").add_code(409).add_details(str(e)).build()
            print('\n', error_instance)
            return False

    def controllGETALL(self, table):
        try:
            return table.getAll()
        except Exception as e:
            error_instance = ErrorBuilder(f"Erro ao buscar dados na tabela: ").add_code(500).add_details(str(e)).build()
            print('\n', error_instance)
            return False

    def controllPUT(self, conditions, data, table):
        try:
            data.validate_data()
            print(data.get_data())
            table.update(conditions, data.get_data())
            return True
        except Exception as e:
            error_instance = ErrorBuilder(f"Erro ao atualizar dados na tabela: ").add_code(500).add_details(str(e)).build()
            print('\n', error_instance)
            return False

    def controllDELETE(self, conditions, table):
        try:
            return table.delete(conditions)
        except Exception as e:
            error_instance = ErrorBuilder(f"Erro ao deletar dados na tabela: ").add_code(500).add_details(str(e)).build()
            print('\n', error_instance)
            return False

    def controllCheckIsDataExists(self, idTable, table):
        try:
            return table.get({"id": idTable})
        except Exception as e:
            error_instance = ErrorBuilder(f"Item não encontrado.").add_code(500).add_details(str(e)).build()
            print('\n', error_instance)
            return False

class LoggingDecorator(ControllerInterface):
    def __init__(self, component):
        self.component = component

    def controllPOST(self, data, table):
        print("Log: Iniciando operação POST")
        result = self.component.controllPOST(data, table)
        print("Log: Operação POST concluída")
        return result

    def controllGET(self, conditions, table):
        print("Log: Iniciando operação GET")
        result = self.component.controllGET(conditions, table)
        print("Log: Operação GET concluída")
        return result

    def controllGETALL(self, table):
        print("Log: Iniciando operação GETALL")
        result = self.component.controllGETALL(table)
        print("Log: Operação GETALL concluída")
        return result

    def controllPUT(self, conditions, data, table):
        print("Log: Iniciando operação PUT")
        result = self.component.controllPUT(conditions, data, table)
        print("Log: Operação PUT concluída")
        return result

    def controllDELETE(self, conditions, table):
        print("Log: Iniciando operação DELETE")
        result = self.component.controllDELETE(conditions, table)
        print("Log: Operação DELETE concluída")
        return result

    def controllCheckIsDataExists(self, idTable, table):
        print("Log: Iniciando operação CheckIsDataExists")
        result = self.component.controllCheckIsDataExists(idTable, table)
        print("Log: Operação CheckIsDataExists concluída")
        return result
