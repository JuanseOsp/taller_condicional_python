minimo_valor = int(input("Ingresa el valor mínimo: "))
maximo_valor = int(input("Ingresa el valor máximo: "))
x = int(input("Ingresa el número x: "))

if minimo_valor <= x <= maximo_valor:
    print(x, "está DENTRO del intervalo")
else:
    print(x, "está FUERA del intervalo")
