from modules.controll.controler import controll
from instance import Instances


def init():
    input_fun = input
    print_fun = print
    allInstances = Instances(input_fun, print_fun)

    tableBuyer = allInstances.getDataPersistenceInstance('.Buyer')
    tableSupermarket = allInstances.getDataPersistenceInstance('.Supermarket')
    tableProduct = allInstances.getDataPersistenceInstance('.Product')

    viewMain = allInstances.getViewMainInstance()
    viewBuyer = allInstances.getViewBuyerInstance()
    viewSupermarket = allInstances.getViewSupermarketInstance()
    viewProduct = allInstances.getViewProductInstance()

    response = 0

    if(tableBuyer == None or tableSupermarket == None or tableProduct == None):
        print("Serviço indisponível...")
        exit()
    else:
        while(response != 4):
            response = viewMain.get_information()
            if (response == 1):
                userBuyer = viewBuyer.get_information()

                res = controll(userBuyer, tableBuyer)
                if(res == True):
                    print_fun("Comprador inserido com sucesso!")
                else:
                    print_fun("Não foi possível inserir o Comprador")


            elif (response == 2):
                userSupermarket = viewSupermarket.get_information()
                res = controll(userSupermarket, tableSupermarket)
                if(res == True):
                    print_fun("Supermercado inserido com sucesso!")
                else:
                    print_fun("Não foi possível inserir o Comprador")

            elif (response == 3):
                product = viewProduct.get_information()
                res = controll(product, tableProduct)
                if(res == True):
                    print_fun("Produto inserido com sucesso!")
                else:
                    print_fun("Não foi possível inserir o produto")
                
            elif (response == 4):
                allInstances.close
                exit()



if __name__ == '__main__':
    init()


