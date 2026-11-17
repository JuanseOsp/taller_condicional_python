tipo = int(input("Tipo de artículo: 1) Textil  2) Electrodoméstico  3) Elementos de cocina  4) Video juego: "))
precio = float(input("¿Cuál es el precio del artículo?: "))

if tipo == 1:
    porcentaje = 0
elif tipo == 2:
    porcentaje = 3.7
elif tipo == 3:
    porcentaje = 4.2
elif tipo == 4:
    porcentaje = 7.8
else:
    porcentaje = -1

if porcentaje < 0:
    print("Tipo de artículo no válido")
else:
    descuento = precio * porcentaje / 100
    print("El descuento es del", porcentaje, "% y equivale a:", descuento)
