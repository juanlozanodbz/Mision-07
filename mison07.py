def hacerMenu():
    print("""Misión 07, Funciones:

    1. Calcular divisiones
    2. Encontrar el mayor
    3. Salir""")
    selection = int(input("Selecciona la función que deseas ejecutar: "))
    return selection

def calcularDivisiones(dentro, fuera):
    sobra = dentro
    resultado = 0

    while sobra >= fuera:
        sobra = sobra - fuera
        resultado = resultado + 1

    print(dentro, "entre", fuera, "es igual a: ", resultado)
    print("Sobran", sobra)



def sacarMayor():
    count = 0
    numero = 0
    while numero != -1:
        numero = int(input("Teclea un valor (-1 para terminar): "))
        if numero >= count:
            count = numero

    if count != 0:
        print("El valor mayor es: ", count)

    else:
        print("No hat valor mayor")



def main():


    selection = hacerMenu()

    while selection != 3:

        if selection == 1:
            dentro = int(input("Introduzca el número a dividir: "))
            fuera = int(input("Introduzca el divisor: "))
            calcularDivisiones(dentro, fuera)

        elif selection == 2:
            sacarMayor()


main()

