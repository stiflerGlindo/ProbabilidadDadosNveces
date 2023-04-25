import random

def lanzar_dados(num_dados):
    suma = 0
    for i in range(num_dados):
        suma += random.randint(1,6)
    return suma

def imprimir_tabla(tabla, imprimir_absolutos, imprimir_porcentajes):
    print("Tabla de Frecuencias:")
    for i in range(2,13):
        if imprimir_absolutos and imprimir_porcentajes:
            print("{0}: {1} ({2:.4f}%)".format(i, tabla[i], tabla[i]/sum(tabla.values())*100))
        elif imprimir_absolutos:
            print("{0}: {1}".format(i, tabla[i]))
        elif imprimir_porcentajes:
            print("{0}: {1:.4f}%".format(i, tabla[i]/sum(tabla.values())*100))

    tabla_prob = {}
    for i in range(2,13):
        tabla_prob[i] = tabla[i]/sum(tabla.values())

    print("\nTabla de Probabilidad:")
    for i in range(2,13):
        print("{0}: {1:.4f}%".format(i, tabla_prob[i]*100))

    tabla_prob_acumulada = {}
    acumulado = 0
    for i in range(2,13):
        acumulado += tabla_prob[i]
        tabla_prob_acumulada[i] = acumulado

    print("\nTabla de Probabilidad Acumulada:")
    for i in range(3,13):
        print("{0}: {1:.4f}".format(i, tabla_prob_acumulada[i]))

# Programa principal
print("Simulador de Lanzamiento de Dados con Análisis Estadístico.")
while True:
    num_lanzamientos = int(input("Ingrese el número de veces que quiere lanzar los dados: "))
    opcion_imprimir = int(input("1. Porcentajes\n2. Valores absolutos\n3. Ambos\nElija una opción de impresión (1, 2 o 3): "))
    num_dados = int(input("Ingrese el número de dados que quiere lanzar: "))

    frecuencias = {i:0 for i in range(2,13)}
    for i in range(num_lanzamientos):
        suma = lanzar_dados(num_dados)
        frecuencias[suma] += 1

    imprimir_tabla(frecuencias, opcion_imprimir in [2,3], opcion_imprimir in [1,3])

    continuar = input("¿Desea volver a tirar los dados? (s/n): ")
    if continuar.lower() == 'n':
        print("¡Gracias por jugar!")
        break
