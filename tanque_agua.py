nivel = float(input("¿Cuántos litros tiene el tanque?: "))

if nivel < 250:
    print("La llave debe ser ABIERTA")
elif nivel > 450:
    print("La llave debe ser CERRADA")
else:
    print("El nivel es correcto, la llave se mantiene como está")
