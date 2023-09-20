salida = False
while salida == False:
    print("Métodos para el cómputo.")
    print("1. For")
    print("2. While")
    metodo = int(input("Escribe el método a usar: "))
    lim = int(input("Escribe el número al que quieras contar: "))
    if metodo == 1:
        # Por cada vez que pase i en el rango entre i y lim+1, aumenta de 1 en 1
        for i in range(0, lim + 1, 2):
            print(i)

    if metodo == 2:
        x = 1
        # Mientras la condición sea verdadera ( Val de X <= lim), se ejecuta lo siguiente
        while x <= lim:
            print(x)
            x = x + 1

    iSalida = int(input("Desea continuar con otra operación ? (1. Si | 2. No ): "))

    if iSalida == 2:
        print("Gracias por utilizarme... como mi ex.")
        salida = True
