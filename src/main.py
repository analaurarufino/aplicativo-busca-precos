from modules.controller.controller import SystemFacade


def init():
    system_facade = SystemFacade()

    response = 0

    while response != 4:
        viewMain = system_facade.instances.getViewMainInstance()
        response = viewMain.get_information()

        if response == 1:
            userBuyer = system_facade.instances.getViewBuyerInstance().get_information()
            res = system_facade.insert_buyer(userBuyer)
            if res:
                print("\nComprador inserido com sucesso!\n")
            else:
                print("Não foi possível inserir o Comprador\n")

        elif response == 2:
            userSupermarket = system_facade.instances.getViewSupermarketInstance().get_information()
            res = system_facade.insert_supermarket(userSupermarket)
            if res:
                print("\nSupermercado inserido com sucesso!\n")
            else:
                print("\nNão foi possível inserir o Supermercado\n")

        elif response == 3:
            product = system_facade.instances.getViewProductInstance().get_information()
            res = system_facade.insert_product(product)
            if res:
                print("\nProduto inserido com sucesso!\n")
            else:
                print("\nNão foi possível inserir o Produto\n")

        elif response == 4:
            system_facade.close()
            exit()


if __name__ == '__main__':
    init()


