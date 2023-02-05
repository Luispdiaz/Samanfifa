from Productos import Productos

class Bebida(Productos):
    def __init__(self, nombre, precio, cantidad, tipo, alcoholica):
        super().__init__(nombre, precio, cantidad, tipo)
        self.alcoholica = alcoholica