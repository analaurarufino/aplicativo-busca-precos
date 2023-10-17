from modules.controller.facede import SystemFacade
from modules.product.product import Product


def init():
    system_facade = SystemFacade(input, print)
    productView = system_facade.instances.getViewProductInstance()

    response = 0

    while response != 7:
        viewMain = system_facade.instances.getViewMainInstance()
        response = viewMain.get_information()

        if response == 1:
            userBuyer = (
                system_facade.instances.getViewBuyerInstance().get_information()
            )  # View recebe as informações
            res = system_facade.insert_buyer(userBuyer)  # Chama facade
            print(res)

        elif response == 2:
            userSupermarket = (
                system_facade.instances.getViewSupermarketInstance().get_information()
            )  # View recebe as informações
            res = system_facade.insert_supermarket(userSupermarket)  # Chama facade
            print(res)

        elif response == 3:
            userProduct = productView.get_information()  # View recebe as informações
            res = system_facade.insert_product(userProduct)  # Chama facade
            print(res)

        elif response == 4:
            idTable = viewMain.get_id()
            res = system_facade.check_product_exists(idTable)  # Chama facade
            if res != False:
                id_product, name, category, price = res
                prod = Product(name, price, category)
                data = productView.get_information_update(prod)
                res = system_facade.update_product(data, idTable)
                print(res)

        elif response == 5:
            res = system_facade.get_all_product()  # Chama facade
            print("\n")
            for i in res:
                print(i)
            print("\n")

        elif response == 6:
            idTable = viewMain.get_id()
            res = system_facade.check_product_exists(idTable)  # Chama facade
            if res != False:
                res = system_facade.delete_product(idTable)
                print("\n", res)

        elif response == 7:
            system_facade.close()
            exit()


if __name__ == "__main__":
    init()
