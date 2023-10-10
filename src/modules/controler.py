from modules.views.mainView import MenuView
from modules.views.supermarketView import SupermarketView
from modules.views.productView import ProductView
from modules.views.buyerView import BuyerView
from modules.database.database import DataPersistence


def init():
    viewMain = MenuView(input, print)
    viewSupermarket = SupermarketView(input, print)
    viewBuyer = BuyerView(input, print)
    viewProduct = ProductView(input, print)
    #Ta lento - trocar para uma conexão
    tableUser = DataPersistence('bppqajxrzzib9zmu6ujp.Buyer')
    tableSuperMarket = DataPersistence('bppqajxrzzib9zmu6ujp.Supermarket')
    tableProduct = DataPersistence('bppqajxrzzib9zmu6ujp.Products')
    response = 0
    while(response != 4):
        response = viewMain.get_information()

        if (response == 1):
            userBuyer = viewBuyer.get_information()
            #Validate userBuyer
            tableUser.insert(userBuyer)
            tableUser.disconnectDB()


        elif (response == 2):
            userSupermarket = viewSupermarket.get_information()
            #Validate userSupermarket
            tableSuperMarket.insert(userSupermarket)
            try:
                tableSuperMarket.disconnectDB()
            except:
                print("Erro ao desconectar")

        elif (response == 3):
            userProduct = viewProduct.get_information()
            #Validate userProduct
            tableProduct.insert(userProduct)
            tableProduct.disconnectDB()
        elif (response == 4):
            exit()

