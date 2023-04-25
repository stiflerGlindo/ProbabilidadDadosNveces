print ('hola mundo') 
import random

def jugar_dados():
    # Inicializar los contadores de cada número
    contadores = [0] * 6
    
    # Tirar los dados 1000 veces
    for _ in range(1000):
        # Generar los dos números aleatorios del 1 al 6
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        # Incrementar los contadores correspondientes
        contadores[dado1-1] += 1
        contadores[dado2-1] += 1
        
    # Imprimir la tabla de frecuencia
    print("Tabla de Frecuencia:")
    print("--------------------")
    for i in range(6):
        probabilidad = contadores[i] / 1000
        print(f"{i+1}: {probabilidad:.2%}")
        
    # Imprimir la tabla de probabilidad acumulada
    print("\nTabla de Probabilidad Acumulada:")
    print("--------------------------------")
    probabilidades = [contadores[i] / 2000 for i in range(6)]
    prob_acumulada = 0
    for i in range(5, -1, -1):
        prob_acumulada += probabilidades[i]
        print(f"{i+1}: {prob_acumulada:.2%}")
        
jugar_dados()


