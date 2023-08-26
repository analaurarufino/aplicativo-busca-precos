from modules.buyer.buyer import addBuyer

def ControllerBuyer(instancias = []):
    emails = []
    loop = True
    while(loop):
        print("Selecione uma opção:\n1 - Adicionar Comprador\n2 - Sair\n")
        choose = input("")
        if(choose == '1'):
            buyerData = addBuyer()
            key = "key_" + buyerData.name
            if(buyerData.email not in emails):
                instancias.append(buyerData)
                emails.append(buyerData.email)
                print("Comprador adicionado com sucesso\n \n")
            else:
                print('\nNão foi possível adicionar o comprador. Email já em uso\n')
        else:
            loop = False

    for elem in instancias:
        elem.print_informations()