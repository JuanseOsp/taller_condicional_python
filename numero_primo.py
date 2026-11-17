n = int(input("Ingresa un número entero entre 0 y 20: "))

if n < 0 or n > 20:
    print("El número está fuera del rango permitido")
elif n in (2, 3, 5, 7, 11, 13, 17, 19):
    print(n, "SÍ es un número primo")
else:
    print(n, "NO es un número primo")
