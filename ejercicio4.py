#Cañificacióm de notas de estudiantes


# Creamos el diccionario con los nombres y las notas de los estudiantes
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# Crear un diccionario vacío para guardar los mensajes finales
student_grades = {}

# Recorremos cada estudiante y su nota en el diccionario original
for estudiante, nota in student_scores.items():

    # Si la nota es de 91 a 100, el resultado es Outstanding
    if nota >= 91:
        grado = "Outstanding"

    # Si no cumplió lo anterior, revisamos si la nota es de 81 a 90
    elif nota >= 81:
        grado = "Exceeds Expectations"

    # Si no cumplió las anteriores, revisamos si es de 71 a 80
    elif nota >= 71:
        grado = "Acceptable"

    # Si la nota es 70 o menor, el estudiante obtiene Fail
    else:
        grado = "Fail"

    # Guardamos el nombre como llave y el mensaje como valor
    student_grades[estudiante] = grado

# Mostramos el diccionario final
print("Diccionario de calificaciones:")
print(student_grades)
# Creamos el diccionario con los nombres y las notas de los estudiantes
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# Creamos un diccionario vacío para guardar los mensajes finales
student_grades = {}

# Recorremos cada estudiante y su nota en el diccionario original
for estudiante, nota in student_scores.items():

    # Si la nota es de 91 a 100, el resultado es Outstanding
    if nota >= 91:
        grado = "Outstanding"

    # Si no cumplió lo anterior, revisamos si la nota es de 81 a 90
    elif nota >= 81:
        grado = "Exceeds Expectations"

    # Si no cumplió las anteriores, revisamos si es de 71 a 80
    elif nota >= 71:
        grado = "Acceptable"

    # Si la nota es 70 o menor, el estudiante obtiene Fail
    else:
        grado = "Fail"

    # Guardamos el nombre como llave y el mensaje como valor
    student_grades[estudiante] = grado

# Mostramos el diccionario final
print("Diccionario de calificaciones:")
print(student_grades)