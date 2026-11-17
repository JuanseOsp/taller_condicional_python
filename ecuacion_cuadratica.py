a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

discriminante = b ** 2 - 4 * a * c

if a != 0 and discriminante >= 0:
    print("La ecuación SÍ tiene solución")
    x1 = (-b + discriminante ** 0.5) / (2 * a)
    x2 = (-b - discriminante ** 0.5) / (2 * a)
    print("x1 =", x1, " x2 =", x2)
else:
    print("La ecuación NO tiene solución")
