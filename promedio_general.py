estudiantes_aprobados = 0
estudiantes_reprobados = 0
conteo_estudiantes = 0
nota_suma = 0

cantidad_estudiantes = int(input("Cuantos estudiantes son: "))

while conteo_estudiantes < cantidad_estudiantes:
    nota = float(input(f"Ingrese la nota del estudiante {conteo_estudiantes + 1}: "))
    if nota >= 3.0:
        estudiantes_aprobados = estudiantes_aprobados + 1
    else:
        estudiantes_reprobados = estudiantes_reprobados + 1
    nota_suma = nota_suma + nota
    conteo_estudiantes = conteo_estudiantes + 1

if cantidad_estudiantes > 0:
    print("Promedio general:", round(nota_suma / cantidad_estudiantes, 2))
    print("Aprobados:", estudiantes_aprobados)
    print("Reprobados:", estudiantes_reprobados)
else:
    print("No hay estudiantes para calcular el promedio")
