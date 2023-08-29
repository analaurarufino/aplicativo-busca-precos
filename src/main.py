from modules.controler import ControllerBuyer
from modules.controler import ControllerSupermarket
instancias = {"buyer": []}

instanciasSM = {"supermarkets": []}


ControllerBuyer(instancias=instancias["buyer"])
ControllerSupermarket(instancias=instanciasSM["supermarkets"])
