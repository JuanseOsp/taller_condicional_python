min1 = int(input("Límite inferior del intervalo 1: "))
max1 = int(input("Límite superior del intervalo 1: "))
min2 = int(input("Límite inferior del intervalo 2: "))
max2 = int(input("Límite superior del intervalo 2: "))
min3 = int(input("Límite inferior del intervalo 3: "))
max3 = int(input("Límite superior del intervalo 3: "))
x = int(input("Ingresa el número x: "))

if min1 < x < max1:
    print(x, "está DENTRO del intervalo 1")
elif min2 < x < max2:
    print(x, "está DENTRO del intervalo 2")
elif min3 < x < max3:
    print(x, "está DENTRO del intervalo 3")
else:
    print(x, "está FUERA de los tres intervalos")
