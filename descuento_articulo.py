precio = float(input("¿Cuál es el precio del artículo?: "))

if precio > 150000:
    descuento = precio * 5 / 100
else:
    descuento = 0

print("El valor del descuento es de:", descuento)
