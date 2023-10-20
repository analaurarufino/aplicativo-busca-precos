from modules.validation.error import CustomError

class Controller:
    def __init__(self):
        pass

    def controllPOST(self, data, table):
        try:
            isValid = data.validate_data()
            if isValid == 0:
                table.insert(data.get_data())
                return True
            else:
                print(CustomError(message=f"Erro de validação: {isValid}"))
                return False
        except Exception as e:
            print(CustomError(message=f"Erro ao inserir dados na tabela: {str(e)}"))
            return False

    def controllGET(self, conditions, table):
        try:
            return table.get(conditions)
        except Exception as e:
            print(CustomError(message=f"Erro ao buscar dados na tabela: {str(e)}"))
            return False

    def controllGETALL(self, table):
        try:
            return table.getAll()
        except Exception as e:
            print(CustomError(message=f"Erro ao buscar dados na tabela: {str(e)}"))
            return False

    def controllPUT(self, conditions, data, table):
        try:
            isValid = data.validate_data()
            if isValid == 0:
                table.update(conditions, data.get_data())
                return True
            else:
                print(CustomError(message=f"Erro de validação: {isValid}"))
                return False
        except Exception as e:
            print(CustomError(message=f"Erro ao atualizar dados na tabela: {str(e)}"))
            return False

    def controllDELETE(self, conditions, table):
        try:
            return table.delete(conditions)
        except Exception as e:
            print(CustomError(message=f"Erro ao deletar dados na tabela: {str(e)}"))
            return False

    def controllCheckIsDataExists(self, idTable, table):
        try:
            return table.get({"id": idTable})
        except Exception as e:
            print(CustomError(message=f"Item não encontrado.\n{str(e)}"))
            return False
