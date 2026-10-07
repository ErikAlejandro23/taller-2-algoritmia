#orden de numeros

# Creamos una función llamada ordenar_lista
def ordenar_lista(lista):

    # Obtenemos la cantidad de elementos que tiene la lista
    n = len(lista)

    # Recorremos la lista varias veces
    for i in range(n):

        # Recorremos los elementos que todavía no están ordenados
        for j in range(0, n - i - 1):

            # Comparamos el elemento actual con el siguiente
            if lista[j] > lista[j + 1]:

                # Guardamos temporalmente el valor actual
                temporal = lista[j]

                # Colocamos el siguiente elemento en la posición actual
                lista[j] = lista[j + 1]

                # Colocamos el valor guardado en la posición siguiente
                lista[j + 1] = temporal

    # Devolvemos la lista ya ordenada
    return lista


# Creamos la lista que nos da el ejercicio
numeros = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

# Mostramos la lista original
print("Lista original:")
print(numeros)

# Llamamos a nuestra propia función para ordenar la lista
resultado = ordenar_lista(numeros.copy())

# Mostramos el resultado obtenido con nuestra función
print("Lista ordenada con nuestra función:")
print(resultado)

# Utilizamos la función predeterminada sorted() de Python
resultado_python = sorted(numeros)

# Mostramos el resultado obtenido con sorted()
print("Lista ordenada con sorted():")
print(resultado_python)

# Comparamos los dos resultados
if resultado == resultado_python:

    # Si son iguales, mostramos que nuestro programa funciona
    print("✓ Nuestra función funciona correctamente.")

else:

    # Si son diferentes, mostramos que hay un error
    print("✗ Los resultados son diferentes.")