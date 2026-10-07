# Compra de helado

precio_helado = 1.90

# Diccionario con los toppings disponibles
opciones = {
    "1": ("Frutas", 0.50),
    "2": ("Granola", 1.50),
    "3": ("Oreo", 1.00),
    "4": ("Brownie", 0.75),
}

print("McDonald's")
print("Helado sin topping vale $1.90")
print()
print("TOPPINGS")
for clave, (nombre, precio) in opciones.items():
    print(f" {clave}. {nombre} - ${precio:.2f}")

# Le pedimos al usuario que seleccione un topping
opcion = input("Seleccione un topping (1-4): ").strip()

if opcion in opciones:
    nombre_topping, precio_topping = opciones[opcion]
    precio_final = precio_helado + precio_topping
    print(f"Elegiste topping de {nombre_topping}.")
else:
    print("Lo sentimos, ese topping no está disponible.")
    precio_final = precio_helado

# Mostramos el precio que debe pagar
print(f"El precio total de su helado es: ${precio_final:.2f}")
