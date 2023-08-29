from modules.buyer.buyer import addBuyer
from modules.supermarket.supermarket import addSupermarket


def ControllerBuyer(instancias=[]):
    emails = []
    loop = True
    while (loop):
        print("Selecione uma opção:\n1 - Adicionar Comprador\n2 - Sair\n")
        choose = input("")
        if (choose == '1'):
            buyerData = addBuyer()
            key = "key_" + buyerData.name
            if (buyerData.email not in emails):
                instancias.append(buyerData)
                emails.append(buyerData.email)
                print("Comprador adicionado com sucesso\n \n")
            else:
                print('\nNão foi possível adicionar o comprador. Email já em uso\n')
        else:
            loop = False

    for elem in instancias:
        elem.print_informations()


def ControllerSupermarket(instancias=[]):
    cnpjs = []
    emails = []
    loop = True
    while loop:
        print("Selecione uma opção:\n1 - Adicionar Supermercado\n2 - Sair\n")
        choose = input("")

        if choose == '1':
            supermarketData = addSupermarket()

            key = "key_" + supermarketData.name

            # Verifica se o email e o CNPJ já estão em uso
            if supermarketData.login not in emails and supermarketData.cnpj not in cnpjs:
                instancias.append(supermarketData)
                emails.append(supermarketData.login)
                cnpjs.append(supermarketData.cnpj)
                print("Supermercado adicionado com sucesso\n \n")
            else:
                print(
                    '\nNão foi possível adicionar o supermercado. Login ou CNPJ já em uso\n')

        else:
            loop = False

    for elem in instancias:
        elem.print_informations()
