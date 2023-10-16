
from modules.validation.error import CustomError

def controll(data, table):
    isValid = data.validate_data()
    if(isValid == 0):
        try:
            table.insert(data.get_data())
            return True
        except:
            print(CustomError(message="Erro ao inserir na tabela Buyer"))
            return False
        
    else:
        print("\n",isValid,"\n")
        return False
    
    

    