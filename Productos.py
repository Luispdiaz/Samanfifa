from SamanFifa import SamanFifa

class Productos(SamanFifa):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre)
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo