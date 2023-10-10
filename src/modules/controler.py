from modules.views.mainView import MenuView
from modules.database.database import Connect
from modules.views.index import BaseView
from modules.views.supermarketView import SupermarketView
from modules.views.productView import ProductView
from modules.views.buyerView import BuyerView
from modules.database.database import DataPersistence


def init(input_fun, print_fun):
    connection = Connect()
    db = connection.connectDB()
    viewMain = MenuView(input_fun, print_fun)
    viewSupermarket = SupermarketView(input_fun, print_fun)
    viewBuyer = BuyerView(input_fun, print_fun)
    viewProduct = ProductView(input_fun, print_fun)
    #Ta lento - trocar para uma conexão
    tableUser = DataPersistence('bppqajxrzzib9zmu6ujp.Buyer', db)
    # tableSuperMarket = DataPersistence('bppqajxrzzib9zmu6ujp.Supermarket')
    # tableProduct = DataPersistence('bppqajxrzzib9zmu6ujp.Products')
    response = 0
    while(response != 4):
        response = viewMain.get_information()

        if (response == 1):
            userBuyer = viewBuyer.get_information()
            isValid = userBuyer.validate_data()

            while(isValid != 0):
                isValid = userBuyer.validate_data()
                if(isValid == 1):
                    print_fun("Nome inválido")
                    userBuyer.set_name(input_fun("Nome: ")) 
                    
                if(isValid == 2):
                    print_fun("\nEmail inválido")
                    userBuyer.set_email(input_fun("Email: "))
                    
                if(isValid == 3):
                    print_fun("Senha inválida")
                    userBuyer.set_password(input_fun("Senha: "))
                    
        

                
            tableUser.insert(userBuyer.get_data())
            #tableUser.disconnectDB()


        elif (response == 2):
            pass
            # userSupermarket = viewSupermarket.get_information()
            # #Validate userSupermarket
            # tableSuperMarket.insert(userSupermarket)
            # try:
            #     tableSuperMarket.disconnectDB()
            # except:
            #     print("Erro ao desconectar")

        elif (response == 3):
            pass
            # userProduct = viewProduct.get_information()
            # #Validate userProduct
            # tableProduct.insert(userProduct)
            # tableProduct.disconnectDB()
        elif (response == 4):
            connection.close(db)
            exit()

