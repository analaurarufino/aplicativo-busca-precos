from modules.controller.facede import SystemFacade
from modules.product.product import Product


def init():
    system_facade = SystemFacade(input, print)
    productView = system_facade.instances.getViewProductInstance()

    response = 0

    while response != 8:
        viewMain = system_facade.instances.getViewMainInstance()
        response = viewMain.get_information()

        if response == 1:
            userBuyer = (
                system_facade.instances.getViewBuyerInstance().get_information()
            )  # View recebe as informações
            res = system_facade.execute_command("insert_buyer",userBuyer)  # Chama facade
            print(res)
            system_facade.execute_command("log_user_action","Adicionar Comprador")

        elif response == 2:
            userSupermarket = (
                system_facade.instances.getViewSupermarketInstance().get_information()
            )  # View recebe as informações
            res = system_facade.execute_command("insert_supermarket", userSupermarket)  # Chama facade
            print(res)
            system_facade.execute_command("log_user_action","Adicionar Supermercado")

        elif response == 3:
            userProduct = productView.get_information()  # View recebe as informações
            res = system_facade.execute_command("insert_product", userProduct)  # Chama facade
            print(res)
            system_facade.execute_command("log_user_action","Adicionar Produto")

        elif response == 4:
            idTable = viewMain.get_id()
            res = system_facade.execute_command("check_product_exists", idTable)  # Chama facade
            if res != False:
                _, name, category, price = res
                prod = Product(name, price, category)
                data = productView.get_information_update(prod)
                res = system_facade.execute_command("update_product", {"product_data":data,"idTable": idTable})
                print(res)
                system_facade.execute_command("log_user_action","Atualizar Produto")

        elif response == 5:
            res = system_facade.execute_command("get_all_product", '')  # Chama facade
            print("\n")
            for i in res:
                print(i)
            print("\n")
            system_facade.execute_command("log_user_action","Acessar Produtos")

        elif response == 6:
            idTable = viewMain.get_id()
            res = system_facade.execute_command("check_product_exists", idTable)  # Chama facade
            if res != False:
                res = system_facade.execute_command("delete_product", idTable)
                print("\n", res)
            system_facade.execute_command("log_user_action","Remover Produto")

        elif response == 7:
            res = system_facade.execute_command("get_report_html", '')
            print(res)
            system_facade.execute_command("log_user_action","Gerar relatorio")

        elif response == 8:
            system_facade.execute_command("close", '')
            exit()


if __name__ == "__main__":
    init()
