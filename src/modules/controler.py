from modules.buyer.buyer import addBuyer
from modules.supermarket.supermarket import addSupermarket


def ControllerBuyer(instancias=[]):
    emails = []
    loop = True
    while (loop == True):
        print("Selecione uma opção:\n1 - Adicionar Comprador\n2 - Sair")
        choose = input("")

        if (choose == '1'):
            buyerData = addBuyer()
            if (buyerData.email not in emails):
                instancias.append(buyerData)
                emails.append(buyerData.email)
                print("Comprador adicionado com sucesso\n \n")
            else:
                print('\nNão foi possível adicionar o comprador. Email já em uso\n')
        else:
            loop = False
            break
    return


def ControllerSupermarket(instancias=[]):
    #cnpjs = []
    logins = []
    loop = True
    while (loop == True):
        print("Selecione uma opção:\n1 - Adicionar Supermercado\n2 - Sair")
        choose = input("")

        if choose == '1':
            supermarketData = addSupermarket()

            # Verifica se o email e o CNPJ já estão em uso
            if (supermarketData.login not in logins):
                instancias.append(supermarketData)
                logins.append(supermarketData.login)
                print("Supermercado adicionado com sucesso\n \n")
            else:
                print(
                    '\nNão foi possível adicionar o supermercado. Login já em uso\n')

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
            for i in instancias['buyer']:
                i.print_informations()
            print("\nFornecedores")
            for e in instancias['supermarkets']:
                e.print_informations()
            print('\n')
        elif (answer == '2'):
            ControllerBuyer(instancias['buyer'])

        elif (answer == '3'):
            ControllerSupermarket(instancias["supermarkets"])

        else:
            loop = False
            break
    return
