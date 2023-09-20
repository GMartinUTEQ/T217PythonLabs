salida = False
while salida == False:
    print("Tenemos dos opciones:")
    print("Suma")
    print("Promedio")
    opcion = input("Escriba la opción que prefiera: ")
    suma = 0
    print(opcion.upper())
    for i in range(5):
        suma += int(input("Escriba un número: "))
    if opcion.upper() == "SUMA":
        print(suma)
    elif opcion.upper() == "PROMEDIO":
        print(suma / 5)
    else:
        print("No seleccionó una opción válida.")

    iSalida = int(input("Desea continuar con otra operación ? (1. Si | 2. No ): "))

    if iSalida == 2:
        print("Gracias por utilizarme... como mi ex.")
        salida = True
