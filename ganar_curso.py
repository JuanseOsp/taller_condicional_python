n1 = float(input("Nota del trabajo 1: "))
n2 = float(input("Nota del trabajo 2: "))
n3 = float(input("Nota del trabajo 3: "))
n4 = float(input("Nota del trabajo 4: "))
n5 = float(input("Nota del trabajo 5: "))

definitiva = (n1 + n2 + n3 + n4 + n5) / 5
print("La nota definitiva es:", round(definitiva, 2))

if definitiva > 3.5:
    print("El estudiante GANÓ el curso")
else:
    print("El estudiante PERDIÓ el curso")
