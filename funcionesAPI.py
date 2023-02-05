import requests
import json
from Equipos import Equipos
from Jugadores import Jugadores
from Arbitros import Arbitros
from Bebida import Bebida
from Comida import Comida
from Estadisticasfutbol import Estadisticasfutbol
from funcionestxt import *


def url():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2122-3/saman_fifa_api/main/api.json"
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        return payload
        
def equipos(payload):
    baseequipos = []
    jsonequipos = payload.get('teams')
    for j in jsonequipos:
        for key,value in j.items():
            if key == "name":
                nombre = value
            if key == "stadium":
                nombreestadio = value['name']
                mapgeneral = value['map']['general']
                mapVIP = value['map']['vip']
        equipo = Equipos(nombre, nombreestadio, mapgeneral, mapVIP)
        baseequipos.append(equipo)
    return baseequipos

def equipos_estadisticas(payload):
    baseestadisticas = []
    jsonequipos = payload.get('teams')
    for j in jsonequipos:
        for key,value in j.items():
            if key == "name":
                nombre = value
            elif key == "lineup":
                for y in value:
                    if y['position'] == 'Goalkeeper':
                        portero = y['name']
        estadistica = Estadisticasfutbol(nombre, 0,0,0, portero)
        baseestadisticas.append(estadistica)
        escribir_estadistica(baseestadisticas)
    return baseestadisticas

        
def arbitros(payload): 
    basearbitros = []
    jsonarbitros = payload.get('referees')
    for i in jsonarbitros:
        arbitro = Arbitros(i)
        basearbitros.append(arbitro)
    return basearbitros
        
def bebida(payload):
    basebebida = []
    base_bebida = []
    jsonrestaurante = payload.get('restaurant')
    for k in jsonrestaurante:
        if k['type'] == 'b':
            bebida = Bebida(k['name'], k['price'], k['quantity'], k['type'], k['alcoholic'])
            base_bebida_txt = [bebida.nombre,bebida.precio,bebida.cantidad,bebida.tipo,bebida.alcoholica]
            base_bebida.append(base_bebida_txt)
            basebebida.append(bebida)
    base_bebida_txt1 = str(base_bebida)
    base_bebida_txt1 = base_bebida_txt1.replace("[","")
    base_bebida_txt1 = base_bebida_txt1.replace("]","")
    base_bebida_txt1 = base_bebida_txt1.replace(",","\n")
    base_bebida_txt1 = base_bebida_txt1.replace("'","")
    escribir_txt(base_bebida_txt1, 'Base_bebida.txt')
    return basebebida

def comida(payload):
    basecomida = []
    base_bebidas_txt = []
    jsonrestaurante = payload.get('restaurant')
    for l in jsonrestaurante:
        if l['type'] == 'c':
            comida = Comida(l['name'], l['price'], l['quantity'], l['type'], l['packing'])
            base_comida_txt = [comida.nombre,comida.precio,comida.cantidad,comida.tipo,comida.embalaje]
            base_bebidas_txt.append(base_comida_txt)
            basecomida.append(comida)
    base_comida_txt1 = str(base_bebidas_txt)
    base_comida_txt1 = base_comida_txt1.replace("[","")
    base_comida_txt1 = base_comida_txt1.replace("]","")
    base_comida_txt1 = base_comida_txt1.replace(",","\n")
    base_comida_txt1 = base_comida_txt1.replace("'","")
    escribir_txt(base_comida_txt1, 'Base_comida.txt')
    return basecomida

def jugadores(payload):
    basejugadores = {}
    jsonequipos = payload.get('teams')
    for h in jsonequipos:
        if h['lineup']:
            basejugadoresequipo = []
            for y in h['lineup']:
                jugador = Jugadores(y['name'], y['number'], y['position'], h['name'], 0)
                basejugadoresequipo.append(jugador)
            basejugadores[h['name']] = basejugadoresequipo
    return basejugadores

def escribir_comida(basecomida):
    basecomida = []
    base_bebidas_txt = []
    for i in basecomida:
        base_comida_txt = [i.nombre,i.precio,i.cantidad,i.tipo,i.embalaje]
        base_bebidas_txt.append(base_comida_txt)
    base_comida_txt1 = str(base_bebidas_txt)
    base_comida_txt1 = base_comida_txt1.replace("[","")
    base_comida_txt1 = base_comida_txt1.replace("]","")
    base_comida_txt1 = base_comida_txt1.replace(",","\n")
    base_comida_txt1 = base_comida_txt1.replace("'","")
    escribir_txt(base_comida_txt1, 'Base_comida.txt')

def escribir_bebida(basebebida):
    base_bebida = []
    base_bebidas_txt = []
    for i in basebebida:
        base_bebida_txt = [i.nombre,i.precio,i.cantidad,i.alcoholica]
        base_bebida.append(base_bebida_txt)
    base_bebida_txt1 = str(base_bebida)
    base_bebida_txt1 = base_bebida_txt1.replace("[","")
    base_bebida_txt1 = base_bebida_txt1.replace("]","")
    base_bebida_txt1 = base_bebida_txt1.replace(",","\n")
    base_bebida_txt1 = base_bebida_txt1.replace("'","")
    escribir_txt(base_bebida_txt1, 'Base_comida.txt')

def escribir_estadistica(baseestadisticas):
    base_estadisticas_txt = []
    for p in baseestadisticas:
        base_estadistica_txt = [p.nombre,p.goles_anotados,p.goles_recibidos,p.partidos_jugados,p.arquero]
        base_estadisticas_txt.append(base_estadistica_txt)
    base_estadisticas_txt1=str(base_estadisticas_txt)
    base_estadisticas_txt1=base_estadisticas_txt1.replace("[","")
    base_estadisticas_txt1=base_estadisticas_txt1.replace("]","")
    base_estadisticas_txt1=base_estadisticas_txt1.replace(",","\n")
    base_estadisticas_txt1=base_estadisticas_txt1.replace("'","")
    escribir_txt(base_estadisticas_txt1,'Base_estadisticas.txt')