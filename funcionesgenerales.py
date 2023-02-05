def validacionstring(msg):
    while True:
        word = input(msg)
        if (word.replace("","")).isalpha():
            return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionint(msg):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcion(msg):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            if word > 3 or word < 0:
                print("El dato que ha ingresado no es valido")
            else:
                return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcion2(msg):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            if word > 2 or word < 0:
                print("El dato que ha ingresado no es valido")
            else:
                return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcion4(msg):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            if word > 4 or word < 0:
                print("El dato que ha ingresado no es valido")
            else:
                return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcion1(msg):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            if word > 1 or word < 0:
                print("El dato que ha ingresado no es valido")
            else:
                return word
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcionstring(msg):
    while True:
        word = input(msg)
        if not word.isnumeric():
                print("El dato que ha ingresado no es valido")
        else:
            return word

def validacionbooleano(msg):
    while True:
        word = input(msg)
        if word.lower() == "si":
            return True
        elif word.lower == "no":
            return False
        else:
            print("El dato que ha ingresado no es valido")

def validacionintopcioncantidad(msg, base, m):
    while True:
        word = input(msg)
        if word.isnumeric():
            word = int(word)
            if word <= base[m].cantidad:
                return word
            else:
                print("Se ha excedido de la cantidad de este producto disponible en el almacen")
        else:
            print("El dato que ha ingresado no es valido")
def numeroperfecto(cedula):
	cont = 0
	for i in range(1,cedula):
		if (cedula % (i) == 0):
			cont += (i)
	if cedula == cont:
		return True
	else:
		return False