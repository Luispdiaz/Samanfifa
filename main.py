from funcionesgenerales import *
from funcionesAPI import *
from funcionesfutbol import *
from funcionesrestaurante import *
from funcionestxt import *
from funcionesestadisticas import *

def main():
    payload = url()
    basearbitros = arbitros(payload) #Extraccion de datos de la API
    baseequipos = equipos(payload)
    basejugadores = jugadores(payload)
    
    if comprobar_txt('Base_comida.txt'): #Extraccion de datos de las API al no haber informacion guardada
        basepartidos = []
        basecomida = comida(payload)
        baseestadisticas = equipos_estadisticas(payload)
        basebebidas = bebida(payload)
        baseclientesVIPestadisticas = []
    else: #Extraccion de datos de los TXT
        baseestadisticas = leer_txt_estadisticas('Base_estadisticas.txt')
        basecomida = leer_txt_comida('Base_comida.txt')
        basebebidas = leer_txt_bebida('Base_bebida.txt')
        basepartidos = leer_txt_partidos('Base_partido.txt')
        butacasVIP = butacasvip(basepartidos, baseequipos)
        butacasGeneral = butacasgeneral(basepartidos, baseequipos)  
        baseclientesVIPestadisticas = leer_txt_cliente('Base_cliente.txt')

    while True:
        bienvenida = "Bienvenido a Saman Fifa"
        bienvenida = bienvenida.center(50,"*")
        print(bienvenida)
        print("\nIngrese el numero de la opcion que corresponda:\n")
        print("Opciones:\n1. Cliente\n2. Administrador \n3. Salir")
        opcion = validacionintopcion("==>")
        if opcion == 1:
            print("\nIngrese el numero de la opcion que corresponda:\n")
            print("Partidos disponibles:\n")
            if len(basepartidos) > 0:
                imprimirpartidosactivos(basepartidos) #Impresion de Partidos Activos
                baseVIP = ventaentradas(basepartidos, butacasVIP, butacasGeneral, basecomida, basebebidas, baseclientesVIPestadisticas) 
                #Procedimiento de recoleccion de datos del cliente, venta de entradas, venta del restaurante y muestra de resultados del partido
                if baseVIP != None:
                    baseclientesVIPestadisticas = baseVIP
            else:
                print("No hay partidos activos")
                continue
        elif opcion == 2:
            print("\nIngrese el numero de la opcion que corresponda:\n")
            print("1. Gestion de los partidos de Futbol\n2. Gestion del Restaurante\n3. Ver estadisticas")
            opcion1 = validacionintopcion("==>")
            if opcion1 == 1:
                print("\nIngrese el numero de la opcion que corresponda:\n")
                print("1. Buscar equipos\n2. Crear partidos\n3. Eliminar partidos\n4. Salir")
                opcion2 = validacionintopcion4("==>")
                if opcion2 == 1:
                    buscarequipos(baseequipos, basejugadores) #Buscar informacion de los equipos en la base de datos 
                elif opcion2 == 2:
                    crearpartidos(baseequipos, basearbitros, basejugadores, basepartidos, baseestadisticas, basejugadores) 
                    #Recoleecion de datos para colocar un partido en "Activo" 
                    butacasVIP = butacasvip(basepartidos, baseequipos) #Creacion de las butacas VIP en el estadio correspondiente 
                    butacasGeneral = butacasgeneral(basepartidos, baseequipos) #Creacion de las butacas general en el estadio correspondiente            
                elif opcion2 == 3:
                    eliminarpartidos(basepartidos) #Eliminar partidos "Activos"
            elif opcion1 == 2:
                print("\nIngrese el numero de la opcion que corresponda:\n")
                print("1. Buscar productos\n2. Ver inventario\n3. Salir")
                opcion2 = validacionintopcion("==>")
                if opcion2 == 1:
                    buscarproductos(basecomida, basebebidas) #Buscar informacion de los productos en la base de datos
                elif opcion2 == 2:
                    imprimirinventario(basecomida, basebebidas) #Imprimir cantidad de productos disponibles
                else:
                    continue
            else:
                print("\nIngrese el numero de la opcion que corresponda:\n")
                print("1.Sobre ventas\n2.Sobre futbol\n3. Salir")
                opcion2 = validacionintopcion("==>")
                if opcion2 == 1:
                    estadisticasventas1(baseclientesVIPestadisticas) #Procedimiento de conteo e impresion de las estadisticas sobre el top de productos mas vendidos
                    estadisticasventas2(baseclientesVIPestadisticas) #Calculo e impresion del promedio de gasto de un cliente VIP
                elif opcion2 == 2:
                    imprimir_tabla_equipos(baseestadisticas) #Procedimiento de conteo e impresion de las tablas con las estadisticas de cada equipo
                    imprimir_arquero(baseestadisticas) #Calculo e impresion del portero que recibio mas goles
                    jugador_mas_goles(basejugadores) #Calculo e impresion del jugador que anoto mas goles
                else:
                    continue          
        else:
            escribir_cerrar(basecomida,basebebidas,baseclientesVIPestadisticas,baseestadisticas) #Escritura de las bases de datos en los TXT al cerrar el programa
            break
    
main()