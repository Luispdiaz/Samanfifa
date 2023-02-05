def estadisticasventas1(baseclientesVIPestadisticas):
    if len(baseclientesVIPestadisticas) == 0:
        print("Todavia no hay estadisticas para mostrar")
    else:
        cantidad_vendidos_santa = 0
        cantidad_vendidos_doritos = 0
        cantidad_vendidos_cheese = 0
        cantidad_vendidos_pack = 0
        cantidad_vendidos_hot= 0
        for i in baseclientesVIPestadisticas:
            for j in i.productoscomprados:
                if j.replace(" ","") == "DobleCheeseBurger":
                    cantidad_vendidos_cheese += 1  
                elif j.replace(" ","") == "SantaTeresa1976":
                    cantidad_vendidos_santa += 1
                elif j.replace(" ","") == "12PackPesis":
                    cantidad_vendidos_pack += 1
                elif j.replace(" ","") == "Doritos":
                    cantidad_vendidos_doritos += 1
                elif j.replace(" ","") == "HotDog":
                    cantidad_vendidos_hot += 1
        cantidades = [cantidad_vendidos_santa, cantidad_vendidos_doritos, cantidad_vendidos_cheese, cantidad_vendidos_pack,cantidad_vendidos_hot]
        cantidades.sort()
        puesto1 = cantidades[-1]
        puesto2 = cantidades[-2]
        puesto3 = cantidades[-3]
        print("Top 3 productos mas vendidos:")
        if puesto1 == 0:
            imprimir_puesto1 = "No hay primer lugar"
        elif puesto1 == cantidad_vendidos_cheese:
            imprimir_puesto1 = "Doble Cheese Burger"
        elif puesto1 == cantidad_vendidos_doritos:
            imprimir_puesto1 = "Doritos"
        elif puesto1 == cantidad_vendidos_hot:
            imprimir_puesto1 = "Hot dogs"
        elif puesto1 == cantidad_vendidos_pack:
            imprimir_puesto1 = "Pack Pesis"
        else:
            imprimir_puesto1 = "1. Santa Teresa"
        if puesto2 == 0:
            imprimir_puesto2 = "No hay segundo lugar"
        elif puesto2 == cantidad_vendidos_cheese and imprimir_puesto1 != "Doble Cheese Burger":
            imprimir_puesto2 = "Doble Cheese Burger"
        elif puesto2 == cantidad_vendidos_doritos and imprimir_puesto1 != "Doritos":
            imprimir_puesto2 ="Doritos"
        elif puesto2 == cantidad_vendidos_hot and imprimir_puesto1 != "Hot dogs":
            imprimir_puesto2 ="Hot dogs"
        elif puesto2 == cantidad_vendidos_pack and imprimir_puesto1 != "12 Pack Pesis":
            imprimir_puesto2 ="12 Pack Pesis"
        elif puesto2 == cantidad_vendidos_santa and imprimir_puesto1 != "Santa Teresa":
            imprimir_puesto2 ="Santa Teresa"
        if puesto3 == 0:
            imprimir_puesto3 = "No hay tercer lugar"
        elif puesto3 == cantidad_vendidos_cheese and imprimir_puesto1 != "Doble Cheese Burger" and imprimir_puesto2 != "Doble Cheese Burger":
            imprimir_puesto3 = "Doble Cheese Burger"
        elif puesto3 == cantidad_vendidos_doritos and imprimir_puesto1 != "Doritos" and imprimir_puesto2 != "Doritos":
            imprimir_puesto3 = "Doritos"
        elif puesto3 == cantidad_vendidos_hot and imprimir_puesto1 != "Hot dogs" and imprimir_puesto2 != "Hot dogs":
            imprimir_puesto3 = "Hot dogs"
        elif puesto3 == cantidad_vendidos_pack and imprimir_puesto1 != "12 Pack Pesis" and imprimir_puesto2 != "12 Pack Pesis":
            imprimir_puesto3 = "12 Pack Pesis"
        elif puesto2 == cantidad_vendidos_santa and imprimir_puesto1 != "Santa Teresa" and imprimir_puesto1 != "Santa Teresa":
            imprimir_puesto3 = "Santa Teresa"
        
        print(f"1. {imprimir_puesto1}\n2. {imprimir_puesto2}\n3. {imprimir_puesto3}")

def estadisticasventas2(baseclientesVIPestadisticas):
    if len(baseclientesVIPestadisticas) != 0:
        contador = len(baseclientesVIPestadisticas)
        aux = 0
        for i in baseclientesVIPestadisticas:
            aux += i.gasto
        total = aux / contador
        print(f"\nPromedio de gasto de un cliente VIP: {total}")


def imprimir_tabla_equipos(baseestadisticas):
    print("***Tabla Equipos***")
    for i in baseestadisticas:
        print(f"\n\t{i.nombre}\n\tPartidos Jugados:{i.partidos_jugados}\n\tGoles anotados:{i.goles_anotados}\n\tGoles Recibidos:{i.goles_recibidos}")

def imprimir_arquero(baseestadisticas):
    mayor = 0
    for i in baseestadisticas:
        if i.goles_recibidos > mayor:
            mayor = i.goles_recibidos
    for j in baseestadisticas:
        if mayor == 0:
            print("Todavia no hay estadisticas para mostrar")
            break
        elif mayor == j.goles_recibidos:
            print("***Portero que recibio mas goles***")
            print(f"Nombre: {j.arquero}\nCantidad: {mayor}")

def jugador_mas_goles(basejugadores):
    mayor = 0
    cont = 0
    for key,value in basejugadores.items():
        for i in value:
            if i.goles > mayor:
                mayor = i.goles
    if mayor != 0:
        print("***Jugadores que anotaron mas goles***")
        for key2,value2 in basejugadores.items():
            for j in value2:
                if mayor == 0:
                    break
                elif j.goles == mayor:
                    print(f"Nombre: {j.nombre}\nCantidad: {mayor}")


    

