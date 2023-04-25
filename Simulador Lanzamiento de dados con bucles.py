import random

def juego_de_dados(num_jugadores, num_tiros):
    jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores.append({'nombre': nombre, 'puntuacion': 0})

    for i in range(num_tiros):
        print(f"\nTurno {i+1}:")
        for jugador in jugadores:
            input(f"Presione enter para que {jugador['nombre']} tire los dados.")
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            puntaje = dado1 + dado2
            jugador['puntuacion'] += puntaje
            print(f"{jugador['nombre']} tiró {dado1}, {dado2}. Puntuación parcial: {jugador['puntuacion']}")
    
    # Encontrar el jugador con la puntuación más alta
    max_puntaje = max(jugador['puntuacion'] for jugador in jugadores)
    ganadores = [jugador['nombre'] for jugador in jugadores if jugador['puntuacion'] == max_puntaje]
    
    # Imprimir resultados finales
    print("\nResultados finales:")
    for jugador in jugadores:
        print(f"{jugador['nombre']}: {jugador['puntuacion']}")
    if len(ganadores) == 1:
        print(f"\nEl ganador es: {ganadores[0]} con {max_puntaje} puntos")
    else:
        print(f"\nEmpate entre los jugadores {', '.join(ganadores)} con {max_puntaje} puntos cada uno")

num_jugadores = int(input("Ingrese el número de jugadores: "))
num_tiros = int(input("Ingrese el número de tiros por jugador: "))
juego_de_dados(num_jugadores, num_tiros)
