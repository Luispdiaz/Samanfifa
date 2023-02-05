from Comida import Comida
from Bebida import Bebida
from Estadisticasfutbol import Estadisticasfutbol
from Partidos import Partidos
from ClienteVIP import ClienteVIP
def leer_txt(archivo):  #En esta funcion se desea leer los datos de un txt auxiliar
    datos = open(archivo, "r")
    mensaje = datos.read() #Con la variable mensaje guardamos la informacion introducida
    datos.close()
    return mensaje

def escribir_txt(mensaje,archivo): #En esta funcion los datos introducidos y recopilados se almacenan 
    datos = open(archivo,'w')       #con un salto de linea en nuestra database.txt
    datos.write(mensaje)
    datos.close


#Metodo para agregar datos de un objeto.
def agregar(self,archivo, archivo_modificado):
    datos = leer_txt(archivo)
    datos += (self.nombre + ','+self.apellido+','+self.cedula+','+str(self.puntaje1)+','+str(self.puntaje2)+','+str(self.puntaje3)+','+str(self.puntaje4)+'\n' )
    escribir_txt(datos, archivo_modificado)

def comprobar_txt(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines() #Con la variable mensaje guardamos la informacion introducida
    if len(mensaje) == 0:
        return True
    else:
        return False

def leer_txt_estadisticas(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines()
    for i in range(len(mensaje)-1):
        mensaje[i] = mensaje[i].replace("\n","")
    mensaje[1] = mensaje[1].replace(" ","")
    mensaje[2] = mensaje[2].replace(" ","")
    mensaje[3] = mensaje[3].replace(" ","")
    mensaje[6] = mensaje[6].replace(" ","")
    mensaje[7] = mensaje[7].replace(" ","")
    mensaje[8] = mensaje[8].replace(" ","")
    mensaje[11] = mensaje[11].replace(" ","")
    mensaje[12] = mensaje[12].replace(" ","")
    mensaje[13] = mensaje[13].replace(" ","")

    objeto1 = Estadisticasfutbol(mensaje[0],int(mensaje[1]),int(mensaje[2]),int(mensaje[3]),mensaje[4])
    objeto2 = Estadisticasfutbol(mensaje[5],int(mensaje[6]),int(mensaje[7]), int(mensaje[8]), mensaje[9])
    objeto3 = Estadisticasfutbol(mensaje[10],int(mensaje[11]),int(mensaje[12]), int(mensaje[13]), mensaje[14])
    base_estadisticas = [objeto1,objeto2,objeto3]
    datos.close()
    return base_estadisticas

def leer_txt_comida(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines() 
    for i in range(len(mensaje)-1):
        mensaje[i] = mensaje[i].replace("\n","")
    mensaje[1] = mensaje[1].replace(" ","")
    mensaje[2] = mensaje[2].replace(" ","")
    mensaje[3] = mensaje[3].replace(" ","")
    mensaje[4] = mensaje[4].replace(" ","")
    mensaje[6] = mensaje[6].replace(" ","")
    mensaje[7] = mensaje[7].replace(" ","")
    mensaje[8] = mensaje[8].replace(" ","")
    mensaje[9] = mensaje[9].replace(" ","")
    mensaje[11] = mensaje[11].replace(" ","")
    mensaje[12] = mensaje[12].replace(" ","")
    mensaje[13] = mensaje[13].replace(" ","")
    mensaje[14] = mensaje[14].replace(" ","")
    objeto1 = Comida(mensaje[0],float(mensaje[1]), int(mensaje[2]), mensaje[3], bool(mensaje[4]))
    objeto2 = Comida(mensaje[5],float(mensaje[6]), int(mensaje[7]), mensaje[8], bool(mensaje[9]))
    objeto3 = Comida(mensaje[10],float(mensaje[11]), int(mensaje[12]), mensaje[13], bool(mensaje[14]))
    base_comida = [objeto1,objeto2,objeto3]
    datos.close()
    return base_comida

def leer_txt_bebida(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines() 
    for i in range(len(mensaje)-1):
        mensaje[i] = mensaje[i].replace("\n","")
    mensaje[1] = mensaje[1].replace(" ","")
    mensaje[2] = mensaje[2].replace(" ","")
    mensaje[3] = mensaje[3].replace(" ","")
    mensaje[4] = mensaje[4].replace(" ","")
    mensaje[6] = mensaje[6].replace(" ","")
    mensaje[7] = mensaje[7].replace(" ","")
    mensaje[8] = mensaje[8].replace(" ","")
    mensaje[9] = mensaje[9].replace(" ","")
    objeto1 = Bebida(mensaje[0],float(mensaje[1]), int(mensaje[2]), mensaje[3], bool(mensaje[4]))
    objeto2 = Bebida(mensaje[5],float(mensaje[6]), int(mensaje[7]), mensaje[8], bool(mensaje[9]))
    base_bebida = [objeto1,objeto2]
    datos.close()
    return base_bebida

def leer_txt_partidos(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines()
    if len(mensaje) == 0:
        basepartidos = []
    else:
        for i in range(len(mensaje)-1):
            mensaje[i] = mensaje[i].replace("\n","")
        mensaje[3] = mensaje[3].replace(" ","")
        mensaje[4] = mensaje[4].replace(" ","")
        mensaje[7] = mensaje[7].replace(" ","")
        mensaje[8] = mensaje[8].replace(" ","")
        objeto1 = Partidos(mensaje[0],mensaje[1],mensaje[2],int(mensaje[3]),int(mensaje[4]),mensaje[5].split("-"),mensaje[6].split("-"),int(mensaje[7]),int(mensaje[8]))
        basepartidos = [objeto1]
    datos.close()
    return basepartidos

def leer_txt_cliente(archivo):
    datos = open(archivo, "r")
    mensaje = datos.readlines() 
    baseclientesVIP = []
    if len(mensaje) == 0:
        baseclientesVIP = []
    elif len(mensaje) == 2:
        for i in range(len(mensaje)-1):
            mensaje[i] = mensaje[i].replace("\n","")
        cont = 0
        for i in range(0,1):
            mensaje[cont] = mensaje[cont].replace(" ","")
            objeto = ClienteVIP(float(mensaje[cont]),mensaje[cont+1].split("-"))
            baseclientesVIP.append(objeto)
            cont += 2
    else:
        for i in range(len(mensaje)-1):
            mensaje[i] = mensaje[i].replace("\n","")
        cont = 0
        for i in range(0, len(mensaje)//2):
            mensaje[cont] = mensaje[cont].replace(" ","")
            objeto = ClienteVIP(float(mensaje[cont]),mensaje[cont+1].split("-"))
            baseclientesVIP.append(objeto)
            cont += 2
    datos.close()
    return baseclientesVIP

def escribir_cerrar(basecomida,basebebidas,baseclientesVIPestadisticas,baseestadisticas):
    base_comidas_txt = []
    for l in basecomida:
        base_comida_txt = [l.nombre,l.precio,l.cantidad,l.tipo,l.embalaje]
        base_comidas_txt.append(base_comida_txt)
    base_comida_txt1 = str(base_comidas_txt)
    base_comida_txt1 = base_comida_txt1.replace("[","")
    base_comida_txt1 = base_comida_txt1.replace("]","")
    base_comida_txt1 = base_comida_txt1.replace(",","\n")
    base_comida_txt1 = base_comida_txt1.replace("'","")
    escribir_txt(base_comida_txt1, 'Base_comida.txt')
    base_bebidas_txt = []
    for i in basebebidas:
        base_bebida_txt = [i.nombre,i.precio,i.cantidad,i.tipo,i.alcoholica]
        base_bebidas_txt.append(base_bebida_txt)
    base_bebida_txt1 = str(base_bebidas_txt)
    base_bebida_txt1 = base_bebida_txt1.replace("[","")
    base_bebida_txt1 = base_bebida_txt1.replace("]","")
    base_bebida_txt1 = base_bebida_txt1.replace(",","\n")
    base_bebida_txt1 = base_bebida_txt1.replace("'","")
    escribir_txt(base_bebida_txt1, 'Base_bebida.txt')
    base_clientes_txt = []
    base_cliente_txt = []
    for h in baseclientesVIPestadisticas:
        base_cliente_txt.append(h.gasto)
        productos = "-".join(h.productoscomprados)
        base_cliente_txt.append(productos)
    base_clientes_txt1 = str(base_cliente_txt)
    base_clientes_txt1 = base_clientes_txt1.replace("[","")
    base_clientes_txt1 = base_clientes_txt1.replace("]","")
    base_clientes_txt1 = base_clientes_txt1.replace(",","\n")
    base_clientes_txt1 = base_clientes_txt1.replace("'","")
    escribir_txt(base_clientes_txt1, 'Base_cliente.txt')
    base_estadisticas_txt = []
    for p in baseestadisticas:
        base_estadistica_txt = [p.nombre,p.goles_anotados,p.goles_recibidos,p.partidos_jugados,p.arquero]
        base_estadisticas_txt.append(base_estadistica_txt)
    base_estadisticas_txt1 = str(base_estadisticas_txt)
    base_estadisticas_txt1 = base_estadisticas_txt1.replace("[","")
    base_estadisticas_txt1 = base_estadisticas_txt1.replace("]","")
    base_estadisticas_txt1 = base_estadisticas_txt1.replace(",","\n")
    base_estadisticas_txt1 = base_estadisticas_txt1.replace("'","")
    escribir_txt(base_estadisticas_txt1, 'Base_estadisticas.txt')
