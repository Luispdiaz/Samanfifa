from funcionesAPI import *
from funcionesgenerales import *

#def main():
 #   payload = url()
    #a = comida(payload)
    #b = bebida(payload)
    #buscarproductos(a, b)

def buscarproductos(a, b):
    print("\nIngrese el numero que corresponda:\n")
    print("1. Comida\n2. Bebida\n3. Salir")
    opcion = validacionintopcion("==>")
    if opcion == 1:
        print("\nIngrese el numero que corresponda para observar mas caracteristicas del producto\n")
        print("Los productos disponibles son los siguientes:\n")
        cont = 0
        for i in a:
            cont += 1
            print(f"{cont}. {i.nombre}")
        opcion = validacionintopcion("==>")
        if opcion == 1:
            for i in a:
                print(f"Nombre del Producto: {i.nombre}")
                print(f"Precio del Producto: {i.precio}$")
                if i.embalaje:
                    print(f"Empaquetado: Si")
                else:
                    print(f"Empaquetado: No")
                break
        elif opcion == 2:
            for i in a:
                if i == a[1]:
                    print(f"Nombre del Producto: {i.nombre}")
                    print(f"Precio del Producto: {i.precio}$")
                    if i.embalaje:
                        print(f"Empaquetado: Si")
                    else:
                        print(f"Empaquetado: No")
        elif opcion == 3:
            for i in a:
                if i == a[2]:
                    print(f"Nombre del Producto: {i.nombre}")
                    print(f"Precio del Producto: {i.precio}$")
                    if i.embalaje:
                        print(f"Empaquetado: Si")
                    else:
                        print(f"Empaquetado: No")
    elif opcion == 2:
        print("\nIngrese el numero que corresponda para observar mas caracteristicas del producto\n")
        print("Los productos disponibles son los siguientes:\n")
        cont = 0
        for i in b:
            cont += 1
            print(f"{cont}. {i.nombre}")
        opcion = validacionintopcion2("==>")    
        if opcion == 1:
            for i in b:
                print(f"Nombre del Producto: {i.nombre}")
                print(f"Precio del Producto: {i.precio}$")
                if i.alcoholica:
                    print(f"Alcoholica: Si")
                else:
                    print(f"Alcoholica: No")
                break
        elif opcion == 2:
            for i in b:
                if i == b[1]:
                    print(f"Nombre del Producto: {i.nombre}")
                    print(f"Precio del Producto: {i.precio}$")
                    if i.alcoholica:
                        print(f"Alcoholica: Si")
                    else:
                        print(f"Alcoholica: No")
#main()
def imprimirinventario(basecomida, basebebida):
    print("\nIngrese el numero que corresponda:\n")
    print("1. Comida\n2. Bebida\n3. Salir")
    opcion = validacionintopcion("==>")
    if opcion == 1:
        print("Inventario comida:")
        print("Nombre   /   Cantidad")
        for i in basecomida:
            print(f"{i.nombre}: {i.cantidad}")
    elif opcion == 2:
        print("Inventario bebida:")
        print("Nombre   /   Cantidad")
        for i in basebebida:
            print(f"{i.nombre}: {i.cantidad}")

