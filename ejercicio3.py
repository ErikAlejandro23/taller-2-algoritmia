#palabra encadenada (piramidal)

# Pedimos al usuario que escriba una palabra
palabra = input("Ingrese una palabra: ")

# Obtenemos la cantidad de letras que tiene la palabra
cantidad = len(palabra)

# Recorremos todas las posibles longitudes de las subcadenas
# Empezamos en 1 y llegamos hasta la cantidad de letras
for longitud in range(1, cantidad + 1):

    # Recorremos las posiciones desde donde puede comenzar
    # una subcadena de la longitud actual
    for inicio in range(0, cantidad - longitud + 1):

        # Obtenemos la subcadena utilizando slicing
        subcadena = palabra[inicio:inicio + longitud]

        # Mostramos la subcadena en pantalla
        print(subcadena)
        