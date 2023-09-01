from modules.buyer.buyer import addBuyer
from modules.supermarket.supermarket import addSupermarket
from modules.database.database import connectDB

try:
    mydb = connectDB()
except:
    print("Não foi possivel conectar ao servidor")

def ControllerBuyer():
    loop = True
    while (loop == True):
        print("Selecione uma opção:\n1 - Adicionar Comprador\n2 - Sair")
        choose = input("")

        if (choose == '1'):
            mycursor = mydb.cursor()
            buyerData = addBuyer()
            sqlCommand = 'INSERT INTO bppqajxrzzib9zmu6ujp.Buyer (name, email, password) VALUES(%s, %s, %s)'
            values = (buyerData.name, buyerData.email,buyerData.password)
            try:
                mycursor.execute(sqlCommand, values)
                mydb.commit()
            except:
                print("Error: Não foi possível inserir o Cliente na tabela")

        else:
            loop = False
            break
    return


def ControllerSupermarket():
    logins = []
    loop = True
    while (loop == True):
        print("Selecione uma opção:\n1 - Adicionar Supermercado\n2 - Sair")
        choose = input("")

        if choose == '1':
            supermarketData = addSupermarket()
            mycursor = mydb.cursor()
            sqlCommand = 'INSERT INTO bppqajxrzzib9zmu6ujp.Supermarket (name, login, password, cnpj) VALUES(%s, %s, %s, %s)'
            values = (supermarketData.name, supermarketData.login,supermarketData.password, supermarketData.cnpj)
            try:
                mycursor.execute(sqlCommand, values)
                mydb.commit()
            except:
                print("Error: Não foi possivel adicionar o Fornecedor")

        else:
            loop = False
            break
    return


def mainControll(instancias={"buyer": [], "supermarkets": []}):
    print("Bem-vindo\nPor favor selecione uma opção para acessar nosse sistema.")

    

    loop = True
    while (loop == True):
        print("1 - Listar todos usuários do sistema\n2 - Acessar Area de Clientes \n3 - Acessar Area de Fornecedores\n4 - Encerrar")
        answer = input("Digite uma opção: ")
        if (answer == "1"):
            print("Clientes")
            mycursor = mydb.cursor()
            try:
                mycursor.execute("SELECT * FROM bppqajxrzzib9zmu6ujp.Buyer")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

                print("\nFornecedores")
                mycursor.execute("SELECT * FROM bppqajxrzzib9zmu6ujp.Supermarket")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)
            except:
                print("Error: Ocorreu um erro ao buscar os usuários na tabela")
            print('\n')
        elif (answer == '2'):
            ControllerBuyer()

        elif (answer == '3'):
            ControllerSupermarket()

        else:
            loop = False
            break
    return
