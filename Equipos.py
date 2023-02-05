from SamanFifa import SamanFifa

class Equipos(SamanFifa):
    def __init__(self, nombre, nombreEstadio, mapGeneral, mapVIP):
        super().__init__(nombre)
        self.nombreEstadio = nombreEstadio
        self.mapGeneral = mapGeneral
        self.mapVIP = mapVIP