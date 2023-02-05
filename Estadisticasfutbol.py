from SamanFifa import SamanFifa
class Estadisticasfutbol(SamanFifa):
    def __init__(self, nombre, goles_anotados, goles_recibidos, partidos_jugados, arquero):
        super().__init__(nombre)
        self.nombre = nombre
        self.goles_anotados = int(goles_anotados)
        self.goles_recibidos = int(goles_recibidos)
        self.partidos_jugados = int(partidos_jugados)
        self.arquero = arquero
        


        