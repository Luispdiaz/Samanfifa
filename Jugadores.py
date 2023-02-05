from socket import NI_NUMERICHOST
from SamanFifa import SamanFifa

class Jugadores(SamanFifa):
    def __init__(self, nombre, numero, posicion, equipo, goles):
        super().__init__(nombre)
        self.numero = numero
        self.posicion = posicion
        self.equipo = equipo
        self.goles = goles
        