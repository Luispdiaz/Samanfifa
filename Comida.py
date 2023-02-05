from Productos import Productos

class Comida(Productos):
    def __init__(self, nombre, precio, cantidad, tipo, embalaje):
        super().__init__(nombre, precio, cantidad, tipo)
        self.embalaje = embalaje