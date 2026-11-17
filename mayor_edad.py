nombre = input("Cual es su nombre: ")
edad = int(input("Cual es su edad: "))

if edad >= 18:
    print(f"Felicidades {nombre}, eres mayor de edad y ya puedes trabajar legalmente")
else:
    print(f"Lo siento {nombre}, eres menor de edad y no puedes ir a una discoteca")
