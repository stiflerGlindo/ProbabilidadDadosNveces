import random
import matplotlib.pyplot as plt

print("\"Simulador de Lanzamiento de Dados con Análisis Estadístico\".")

n = int(input("Ingrese el número de veces que quiere lanzar el dado: "))
lanzamientos = [random.randint(1, 6) for _ in range(n)]

frecuencias = [lanzamientos.count(i) for i in range(1, 7)]
porcentajes = [f"{(frecuencia/n)*100:.2f}%" for frecuencia in frecuencias]

acumulado = 0
prob_acumulada = []
for frecuencia in frecuencias[::-1]:
    acumulado += frecuencia/n
    prob_acumulada.append(f"{acumulado*100:.2f}%")

print("\nTabla de Frecuencia:")
print("--------------------")
for i in range(6):
    print(f"{i+1}: {porcentajes[i]}")

print("\nTabla de Probabilidad Acumulada:")
print("--------------------------------")
for i in range(6):
    print(f"{6-i}: {prob_acumulada[i]}")
print("--------------------------------")

opcion = int(input("1. Porcentajes\n2. Valores absolutos\nElija una opción de impresión (1 o 2): "))
if opcion == 1:
    print("\n¡Gracias por jugar a los dados!")
elif opcion == 2:
    print("\nTabla de Frecuencia:")
    print("--------------------")
    for i in range(6):
        print(f"{i+1}: {frecuencias[i]}")
    print("\nTabla de Probabilidad Acumulada:")
    print("--------------------------------")
    for i in range(6):
        print(f"{6-i}: {frecuencias[::-1][i]/n*100:.2f}%")
    print("--------------------------------")
    input("\nPresione Enter para salir.")
else:
    print("\nOpción inválida. ¡Gracias por jugar a los dados!")


