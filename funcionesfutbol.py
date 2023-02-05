from ClienteVIP import ClienteVIP
from funcionesAPI import *
from funcionesgenerales import *
from Partidos import Partidos
import random
import numpy as np
from Estadisticasfutbol import Estadisticasfutbol

#def main():
   #payload = url()
   #a = equipos(payload)
   #b = jugadores(payload)
   #c = arbitros(payload)
   #d = crearpartidos(a, c, b, basepartidos)
   #ventaentradas(a, d)


def buscarequipos(a, b):
    print("\nIngrese el numero que corresponda para observar mas caracteristicas del equipo\n")
    print("Los equipos disponibles son los siguientes:")
    cont = 0
    for i in a:
        cont += 1
        print(f"{cont}. {i.nombre}")
    opcion = validacionint("==>")
    if opcion == 1:
        for i in a:
            print(f"Nombre del equipo: {i.nombre}")
            print(f"Nombre del Estadio: {i.nombreEstadio}")
            print(f"Capacidad de entradas generales: {i.mapGeneral}")
            print(f"Capacidad de entradas VIP: {i.mapVIP}")
            break
        opcion1 = validacionint("Si quiere ver la alineacion del equipo ingrese 1, en su defecto, otro numero:")
        if opcion1 == 1:
            for j in a:
                if j == a[0]:
                    for key, value in b.items():
                        if key == j.nombre:
                            for x in value:
                                print(f"\nNombre:{x.nombre}")
                                print(f"Numero:{x.numero}")
                                print(f"Posicion:{x.posicion}\n")

    elif opcion == 2:
        for i in a:
            if i == a[1]:
                print(f"Nombre del equipo: {i.nombre}")
                print(f"Nombre del Estadio: {i.nombreEstadio}")
                print(f"Capacidad de entradas generales: {i.mapGeneral}")
                print(f"Capacidad de entradas VIP: {i.mapVIP}")
        opcion1 = validacionint("Si quiere ver la alineacion del equipo ingrese 1, en su defecto, otro numero:")
        if opcion1 == 1:
            for j in a:
                if j == a[1]:
                    for key, value in b.items():
                        if key == j.nombre:
                            for x in value:
                                print(f"\nNombre:{x.nombre}")
                                print(f"Numero:{x.numero}")
                                print(f"Posicion:{x.posicion}\n")
            
    elif opcion == 3:
        for i in a:
            if i == a[2]:
                print(f"Nombre del equipo: {(i+2).nombre}")
                print(f"Nombre del Estadio: {(i+2).nombreestadio}")
                print(f"Capacidad de entradas generales: {(i+2).mapgeneral}")
                print(f"Capacidad de entradas VIP: {(i+2).mapVIP}")
        opcion1 = validacionint("Si quiere ver la alineacion del equipo ingrese 1, en su defecto, otro numero:")
        if opcion1 == 1:
            for j in a:
                if j == a[2]:
                    for key, value in b.items():
                        if key == j.nombre:
                            for x in value:
                                print(f"\nNombre:{x.nombre}")
                                print(f"Numero:{x.numero}")
                                print(f"Posicion:{x.posicion}\n")

def crearpartidos(a, c, b, basepartidos, baseestadisticas, basejugadores):
    if len(basepartidos) == 0:
        print("Ingrese el numero del equipo que corresponda para crear el partido:")
        cont = 0
        for i in a:
            cont += 1
            print(f"{cont}. {i.nombre}")
        print("Equipo 1:")
        opcionequipo1 = validacionintopcion("==>")
        if opcionequipo1 == 1:
            for i in a:
                if i == a[0]:
                    equipo1 = i.nombre
        elif opcionequipo1 == 2:
            for i in a:
                if i == a[1]:
                    equipo1 = i.nombre
        elif opcionequipo1 == 3:
            for i in a:
                if i == a[2]:
                    equipo1 = i.nombre
        print("Equipo 2:")
        while True:
            opcionequipo2 = validacionintopcion("==>")
            if opcionequipo1 == opcionequipo2:
                print("Ya haz elegido ese equipo.")
            else:
                if opcionequipo2 == 1:
                    for i in a:
                        equipo2 = i.nombre
                        break
                    break
                elif opcionequipo2 == 2:
                    for i in a:
                        if i == a[1]:
                            equipo2 = i.nombre
                    break
                elif opcionequipo2 == 3:
                    for i in a:
                        if i == a[2]:
                            equipo2 = i.nombre
                    break
        print("Estadio:")
        if opcionequipo1 > opcionequipo2:
            for j in a:
                if j == a[opcionequipo1-1]:
                    imprimir1 = f"1. {j.nombreEstadio}"
                elif j == a[opcionequipo2-1]:
                    imprimir2 = f"2. {j.nombreEstadio}"
            print(imprimir1)
            print(imprimir2)
        elif opcionequipo1 < opcionequipo2:
            for m in a:
                if m == a[opcionequipo1-1]:
                    print(f"1. {m.nombreEstadio}")
                elif m == a[opcionequipo2-1]:
                    print(f"2. {m.nombreEstadio}")
        opcionestadio = validacionintopcion2("==>")
        if opcionestadio == 1:
            for i in a:
                if i == a[opcionequipo1-1]:
                    estadio = i.nombreEstadio
        elif opcionestadio == 2:
            for l in a:
                if l == a[opcionequipo2-1]:
                    estadio = l.nombreEstadio
        arbitro = random.choice(c)
        print(f"Informacion del partido:{equipo1} vs {equipo2}\n")
        print(f"-Equipo 1: {equipo1}")
        print(f"-Alineacion:")
        for j in a:
            if j == a[opcionequipo1-1]:
                for key, value in b.items():
                            if key == j.nombre:
                                for x in value:
                                    print(f"\n\tNombre:{x.nombre}")
                                    print(f"\tNumero:{x.numero}")
                                    print(f"\tPosicion:{x.posicion}\n")
        print(f"\n-Equipo 2: {equipo2}")
        print(f"-Alineacion:")
        for k in a:
            if k == a[opcionequipo2-1]:
                for key, value in b.items():
                            if key == k.nombre:
                                for y in value:
                                    print(f"\n\tNombre:{y.nombre}")
                                    print(f"\tNumero:{y.numero}")
                                    print(f"\tPosicion:{y.posicion}\n")
        print(f"-Estadio: {estadio}")
        print(f"-Arbitro: {arbitro.nombre}")
        golesequipo1 = random.randint(1, 9)
        listagoleadoresequipo1 = []
        for g in range(golesequipo1):
            goleador1 =  random.choice(b[equipo1])
            goleador1.goles += 1
            listagoleadoresequipo1.append(goleador1.nombre)
        golesequipo2 = random.randint(1, 9) 
        listagoleadoresequipo2 = []
        for g in range(golesequipo2):
            goleador2 =  random.choice(b[equipo1])
            goleador2.goles += 1
            listagoleadoresequipo2.append(goleador2.nombre)
        
        precioentradageneral = validacionint("Ingrese el precio de la entrada general:\n==>")
        precioentradaVIP = validacionint("Ingrese el precio de la entrada VIP:\n==>")
        objeto = Partidos(equipo1, equipo2, estadio, golesequipo1, golesequipo2, listagoleadoresequipo1, listagoleadoresequipo2, precioentradageneral, precioentradaVIP)
        basepartidos.append(objeto)
        for i in baseestadisticas:
            if equipo1 == i.nombre:
                i.goles_anotados += golesequipo1
                i.goles_recibidos += golesequipo2
                i.partidos_jugados += 1
            elif equipo2 == i.nombre:
                i.goles_anotados += golesequipo2
                i.goles_recibidos += golesequipo1
                i.partidos_jugados += 1
        base_partidos_txt = []
        base_partido = []
        goleadores1 = ''
        goleadores2 = ''
        for t in basepartidos:
            base_partido.append(t.equipo1)
            base_partido.append(t.equipo2)
            base_partido.append(t.estadio)
            base_partido.append(t.golesequipo1)
            base_partido.append(t.golesequipo2)
            goleadores1 = "-".join(t.goleadoresequipo1)
            base_partido.append(goleadores1)
            goleadores2 = "-".join(t.goleadoresequipo2)
            base_partido.append(goleadores2)
            base_partido.append(t.precioentradageneral)
            base_partido.append(t.precioentradaVIP)
            base_partidos_txt.append(base_partido)
        base_partido_txt1 = str(base_partidos_txt)
        base_partido_txt1 = base_partido_txt1.replace("[","")
        base_partido_txt1 = base_partido_txt1.replace("]","")
        base_partido_txt1 = base_partido_txt1.replace(",","\n")
        base_partido_txt1 = base_partido_txt1.replace("'","")
        escribir_txt(base_partido_txt1, 'Base_partido.txt')
    else:
        print("No hay suficientes equipos disponibles para crear un partido")

def mostrarresultados(basepartidos):
    print("***Partido***")
    for i in basepartidos:
        if i.golesequipo1 > i.golesequipo2:
            print(f"El Equipo {i.equipo1} ha ganado")
            print(f"Goleadores de {i.equipo1}:")
            for j in i.goleadoresequipo1:
                print(f"\t-> {j}")
            print(f"Goleadores de {i.equipo2}:")
            for q in i.goleadoresequipo2:
                print(f"\t-> {q}")
            print(f"Resultado final:\n\t{i.equipo1} {i.golesequipo1} - {i.equipo2} {i.golesequipo2}")
        elif i.golesequipo1 < i.golesequipo2:
            print(f"El Equipo {i.equipo2} ha ganado")
            print(f"Goleadores de {i.equipo1}:")
            for j in i.goleadoresequipo1:
                print(f"\t-> {j}")
            print(f"Goleadores de {i.equipo2}:")
            for q in i.goleadoresequipo2:
                print(f"\t->{q}")
            print(f"Resultado final:\n\t{i.equipo1} {i.golesequipo1} - {i.equipo2} {i.golesequipo2}")
        else:
            print(f"El partido ha quedado en empate")
            print(f"Goleadores de {i.equipo1}:")
            for j in i.goleadoresequipo1:
                print(f"\t-> {j}")
            print(f"Goleadores de {i.equipo2}:")
            for q in i.goleadoresequipo2:
                print(f"\t->{q}")
            print(f"Resultado final:\n\t{i.equipo1} {i.golesequipo1} - {i.equipo2} {i.golesequipo2}")                

def eliminarpartidos(basepartidos):
    aux = True
    if len(basepartidos) > 0:
        cont = 0
        for i in basepartidos:
            cont += 1
            print("Partidos Activos:")
            print(f"{cont}. {i.equipo1} vs {i.equipo2}")
            print(f"Estadio:{i.estadio}")
            print(f"Precio entrada general: {i.precioentradageneral}")
            print(f"Precio entrada VIP: {i.precioentradaVIP}")

        opcioneliminar = validacionint("Ingrese el numero del partido que desea eliminar:\n==>")
        if opcioneliminar > len(basepartidos) or opcioneliminar < len(basepartidos):
            print("El dato que ha ingresado no es valido")
        else:
            basepartidos.pop(opcioneliminar-1)
            escribir_txt("","Base_partido.txt")
    else:
        print("No hay partidos activos")

def imprimirpartidosactivos(basepartidos):
    if len(basepartidos) > 0:
        cont = 0
        for i in basepartidos:
            cont += 1
            print("Partidos Activos:")
            print(f"{cont}. {i.equipo1} vs {i.equipo2}")
            print(f"Estadio:{i.estadio}")
            print(f"Precio entrada general: {i.precioentradageneral}")
            print(f"Precio entrada VIP: {i.precioentradaVIP}")
    else:
        print("No hay partidos activos")


def butacasvip(basepartidos, baseequipos):
    for i in basepartidos:
            for j in baseequipos:
                if i.estadio == j.nombreEstadio:
                    cantidadbutacasvip = j.mapVIP
                elif i.estadio == " "+j.nombreEstadio:
                    cantidadbutacasvip = j.mapVIP
    butacasVIP = []
    for i in range(cantidadbutacasvip[0]):
        lista = []
        butacasVIP.append(lista)
        for j in range(cantidadbutacasvip[1]):
            lista.append("O")
    return butacasVIP

def butacasgeneral(basepartidos, baseequipos):
    for i in basepartidos:
                for j in baseequipos:
                    if i.estadio == j.nombreEstadio:
                        cantidadbutacasgeneral = j.mapGeneral
                    elif i.estadio == " "+j.nombreEstadio:
                        cantidadbutacasgeneral = j.mapGeneral
    butacasgeneral = []
    for i in range(cantidadbutacasgeneral[0]):
        lista = []
        butacasgeneral.append(lista)
        for j in range(cantidadbutacasgeneral[1]):
            lista.append("O")
    return butacasgeneral

def permutaciones(numero):
    permutaciones = []
    for j in range(len(numero)):
        for i in numero:
            combinacion = numero[j] + i
            permutaciones.append(combinacion)
    return permutaciones
    
def vampiro(numero, aux, aux1):
    for i in range(len(aux)):
        for j in range(len(aux)):
            if i == j:
                continue
            else:
                if int(aux[i]) * int(aux[j]) == int(numero):
                    aux1 = True
    return aux1


def ventaentradas(basepartidos, butacasVIP, butacasgeneral, basecomida, basebebidas, baseclientesVIPestadisticas):
    puestos = []
    aux1 = False
    opcionpartido = validacionintopcion1("==>")
    print(f"Tipo de Entrada:\n1. General: {basepartidos[0].precioentradageneral}\n2. VIP: {basepartidos[0].precioentradaVIP}")
    opcionentrada = validacionintopcion2("==>")
    if opcionentrada == 1:
        print("Ingrese los siguientes datos:")
        nombre = validacionstring("Nombre completo: ")
        cedula = validacionintopcionstring("Cedula: ")
        edad = validacionint("Edad: ")
        cantidadentradas = validacionint("Cantidad de entradas:")
        costoentrada = cantidadentradas * basepartidos[0].precioentradageneral
        cedulavampiro = permutaciones(cedula)
        aux5 = vampiro(cedula, cedulavampiro, aux1)
        if aux5 == True:
            costoentradacondescuento = costoentrada * 0.50
            costoentradadescuentoIVA = costoentradacondescuento + costoentradacondescuento * 0.16
        else:
            costoentradaIVA = costoentrada + costoentrada * 0.16
        butacasgeneral1 = np.array(butacasgeneral)
        print("Los asientos disponibles son los siguientes:")
        print(butacasgeneral1)
        for i in range(cantidadentradas):
            aux = False
            while aux == False:
                print(f"Entrada {i+1}\nIngrese numero de fila:")
                fila = int(validacionint("==>"))
                if fila > len(butacasgeneral) or fila < 0:
                    print("El dato que ha ingresado no es valido")
                    continue
                else:
                    print("Ingrese numero de columna:")
                    columna = int(validacionint("==>"))
                    if columna > len(butacasgeneral[0]) or columna < 0:
                        print("El dato que ha ingresado no es valido")
                        continue
                    else:
                        for h in butacasgeneral:
                            if h == butacasgeneral[fila-1]:
                                for m in h:
                                    if m == h[columna-1]:
                                        if m != "O":
                                            print("El asiento ya esta ocupado")
                                        else:
                                            h[columna-1] = "X"
                                            aux = True
                                            puestos.append([fila,columna])
                                            break
                                break
        print("***Factura***")
        print("Puestos:")
        for c in puestos:
            print(f"\t* Fila: {c[0]} - Columna: {c[1]}")
        print("Informacion de pago:")
        if aux5 == True:
            print(f"Subtotal: {costoentrada}")
            print(f"Descuento: 50%")
            print(f"IVA: 16%")
            print(f"Total: {costoentradadescuentoIVA}")
        else:
            print(f"Subtotal: {costoentrada}")
            print(f"Descuento: No aplica")
            print(f"IVA: 16%")
            print(f"Total: {costoentradaIVA}")
        print("Si desea pagar ingrese 1, en su defecto, ingrese otro numero:")
        opcionpagar = validacionint("==>")
        if opcionpagar == 1:
            print("Su compra ha sido exitosa")
            mostrarresultados(basepartidos)
        else:
            print("Compra denegada")
            for n in puestos:
                for h in butacasgeneral:
                    if h == butacasgeneral[n[0]-1]:
                        for m in h:
                            if m == h[n[1]-1]:
                                h[n[1]-1] = "O"
            
    elif opcionentrada == 2:
        precio_cliente_total = 0
        print("Ingrese los siguientes datos:")
        nombre = validacionstring("Nombre completo: ")
        cedula = validacionintopcionstring("Cedula: ")
        edad = validacionint("Edad: ")
        cantidadentradas = validacionint("Cantidad de entradas:")
        costoentrada = cantidadentradas * basepartidos[0].precioentradaVIP
        cedulavampiro = permutaciones(cedula)
        aux5 = vampiro(cedula, cedulavampiro, aux1)
        if aux5:
            costoentradacondescuento = costoentrada * 0.50
            costoentradadescuentoIVA = costoentradacondescuento + costoentradacondescuento * 0.16
        else:
            costoentradaIVA = costoentrada + costoentrada * 0.16
        butacasVIP1 = np.array(butacasVIP)
        print("Los asientos disponibles son los siguientes:")
        print(butacasVIP1)
        for i in range(cantidadentradas):
            aux = False
            while aux == False:
                print(f"Entrada {i+1}\nIngrese numero de fila:")
                fila = int(input("==>"))
                if fila > len(butacasVIP) or fila < 0:
                    print("El dato que ha ingresado no es valido")
                    continue
                else:
                    print("Ingrese numero de columna:")
                    columna = int(input("==>"))
                    if columna > len(butacasVIP[0]) or columna < 0:
                        print("El dato que ha ingresado no es valido")
                        continue
                    else:
                        for h in butacasVIP:
                                    if h == butacasVIP[fila-1]:
                                        for m in h:
                                            if m == h[columna-1]:
                                                if m != "O":
                                                    print("El asiento ya esta ocupado")
                                                else:
                                                    h[columna-1] = "X"
                                                    aux = True
                                                    puestos.append([fila,columna])
                                                    break
                                        break
        print("***Factura***")
        print("Puestos:")
        for c in puestos:
            print(f"\t* Fila: {c[0]} - Columna: {c[1]}")
        print("Informacion de pago:")
        if aux5:
            print(f"Subtotal: {costoentrada}")
            print(f"Descuento: 50%")
            print(f"IVA: 16%")
            print(f"Total: {costoentradadescuentoIVA}")
            precio_cliente_total += costoentradadescuentoIVA
        else:
            print(f"Subtotal: {costoentrada}")
            print(f"Descuento: No aplica")
            print(f"IVA: 16%")
            print(f"Total: {costoentradaIVA}")
            precio_cliente_total += costoentradaIVA
        print("Si desea pagar ingrese 1, en su defecto, ingrese otro numero:")
        opcionpagar = validacionint("==>")
        if opcionpagar == 1:
            print("Su compra ha sido exitosa")
            print("***Comienza el partido***")
            print("***Restaurante Saman Fifa***")
            print("Si desea consumir algun producto del restaurante ingrese 1, en su defecto ingrese otro numero:")
            rest = validacionint("==>")
            if rest == 1:
                pedido = []
                pedido_objeto = []
                while True:
                    print("\nIngrese el numero que corresponda:\n")
                    print("1. Comida\n2. Bebida")
                    opcion = validacionintopcion("==>")
                    if opcion == 1:
                        cont = 0
                        for i in basecomida:
                            cont += 1
                            print(f"{cont}. {i.nombre}")
                            print(f"Precio del Producto: {i.precio}$")
                        print("Ingrese el numero que corresponda:")
                        opcion = validacionintopcion("==>")
                        if basecomida[opcion-1].cantidad == 0:
                            print("El producto se ha agotado")
                        else:
                            print("Cantidad:")
                            opcioncantidad = validacionintopcioncantidad("==>", basecomida, opcion-1)
                            while opcioncantidad > 0:
                                for j in range(len(basecomida)):
                                    if j == opcion - 1:
                                        pedido.append(basecomida[j])
                                        pedido_objeto.append(basecomida[j].nombre)
                                        opcioncantidad -= 1
                                        basecomida[j].cantidad = basecomida[j].cantidad - 1
                        print("Si quiere realizar otro pedido, ingrese 1, en su defecto otro numero:")
                        opcion2 = validacionint("==>")
                        if opcion2 == 1:
                            continue
                        else:
                            break
                    elif opcion == 2: 
                        print("\nIngrese el numero que corresponda para observar mas caracteristicas del producto\n")
                        print("Los productos disponibles son los siguientes:\n")
                        cont4 = 0
                        for i in basebebidas:
                            cont4 += 1
                            print(f"{cont4}. {i.nombre}")
                            print(f"Precio del Producto: {i.precio}$")
                        opcion = validacionintopcion("==>")
                        if basebebidas[opcion-1].cantidad == 0:
                            print("El producto se ha agotado")
                        else:
                            print("Cantidad:") 
                            opcioncantidad = validacionintopcioncantidad("==>", basebebidas, opcion-1)
                            while opcioncantidad > 0:
                                for h in range(len(basebebidas)):
                                    if h == opcion - 1:
                                        pedido.append(basebebidas[h])
                                        pedido_objeto.append(basebebidas[h].nombre)
                                        opcioncantidad -= 1 
                                        basebebidas[h].cantidad = basebebidas[h].cantidad - 1
                        print("Si quiere realizar otro pedido, ingrese 1, en su defecto otro numero:")
                        opcion2 = validacionint("==>")
                        if opcion2 == 1:
                            continue
                        else:
                            break
                print("***Informacion del pedido***")
                informacionpedido = {}
                for x in pedido:
                    informacionpedido[x] = {'cantidad':0, 'precio': 0}
                for l in pedido:
                    for key5,value5 in informacionpedido.items():
                        if l == key5:
                            value5['cantidad'] += 1
                        else:
                            continue
                for g,e in informacionpedido.items():
                    e['precio'] = g.precio * e['cantidad']
                            
                preciototal = 0
                for key,value in informacionpedido.items():
                    print(f"\n\tNombre:{key.nombre}")
                    print(f"\tCantidad:{value['cantidad']}")
                    print(f"\tCosto:{value['precio']}")
                    preciototal += value['precio']
                            
                    if numeroperfecto(int(cedula)):
                        print(f"\nPrecio total: {preciototal*0.15}")
                    else:
                        print(f"\nPrecio total: {preciototal}")
                print("Si desea pagar ingrese 1, en su defecto, ingrese otro numero:")
                opcionpagar = validacionint("==>")
                if opcionpagar == 1:
                    print("Su compra ha sido exitosa")
                    print("***Factura***")
                    if numeroperfecto(int(cedula)):
                        print(f"Subtotal: {preciototal}")
                        print(f"Descuento: 15%")
                        print(f"Precio total: {preciototal*0.15}")
                        precio_cliente_total += preciototal*0.15
                    else:
                        print(f"Subtotal: {preciototal}")
                        print(f"Descuento: No aplica")
                        print(f"Precio total: {preciototal}")
                        precio_cliente_total += preciototal
                    mostrarresultados(basepartidos)
                else:
                    print("Compra denegada")
                    for key1,value1 in informacionpedido.items():
                        key1.cantidad += value1['cantidad']
                objeto_clente = ClienteVIP(precio_cliente_total,pedido_objeto)
                baseclientesVIPestadisticas.append(objeto_clente)
        else:
            print("Compra denegada")
            for n in puestos:
                for h in butacasVIP:
                    if h == butacasVIP[n[0]-1]:
                        for m in h:
                            if m == h[n[1]-1]:
                                h[n[1]-1] = "O" 
        return baseclientesVIPestadisticas
                

            
        
            
                            
                            

#main()