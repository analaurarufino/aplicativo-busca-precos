from modules.database.database import DatabaseFactory, DataPersistence
from modules.views.supermarketView import SupermarketView
from modules.views.productView import ProductView
from modules.views.buyerView import BuyerView
from modules.views.mainView import MenuView
from modules.config.config import Config
from modules.validation.error import CustomError


class Instances:
    _instance = None

    def __new__(cls, input_fun, print_fun):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(input_fun, print_fun)
        return cls._instance

    def _initialize(self, input_fun, print_fun):
        try:
            # Carregar configurações
            config = Config("src/config.txt")
            host, user, password, self.prefix_table = (
                config.get_host(),
                config.get_user(),
                config.get_password(),
                config.get_prefix_table(),
            )

            # Inicializar a base de dados
            self.db, self.close = self.initialize_database(host, user, password)
        except CustomError as e:
            print(f"Erro ao inicializar: {e}")

        # Inicializar as views
        self.viewMain = MenuView(input_fun, print_fun)
        self.viewSupermarket = SupermarketView(input_fun, print_fun)
        self.viewBuyer = BuyerView(input_fun, print_fun)
        self.viewProduct = ProductView(input_fun, print_fun)

    def initialize_database(self, host, user, password):
        try:
            # Conectar à base de dados
            factory = DatabaseFactory()
            connection = factory.create_database("mysql")
            db = connection.connectDB(host=host, password=password, username=user)
            return db, connection.close
        except Exception as e:
            raise CustomError(f"Não foi possível conectar à base de dados: {str(e)}")

    def getDataPersistenceInstance(self, prefix_table):
        try:
            res = DataPersistence(self.prefix_table + prefix_table, self.db)
            return res
        except Exception as e:
            print(CustomError(f"Não foi possível conectar à tabela: {str(e)}"))
            print("Por favor, tente mais tarde.")

    def getDBInstance(self):
        return self.db

    def getTableUserInstance(self):
        return self.tableUser

    def getViewMainInstance(self):
        return self.viewMain

    def getViewSupermarketInstance(self):
        return self.viewSupermarket

    def getViewBuyerInstance(self):
        return self.viewBuyer

    def getViewProductInstance(self):
        return self.viewProduct
