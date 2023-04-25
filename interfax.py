import pygame
import random

pygame.init()

# Define los colores que utilizaremos en la interfaz
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define las dimensiones de la ventana
WIDTH = 400
HEIGHT = 300

# Crea la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define el título de la ventana
pygame.display.set_caption("Juego de Dados")

# Define las fuentes que utilizaremos en la interfaz
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Define la función para lanzar los dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    puntaje = dado1 + dado2
    return (dado1, dado2, puntaje)

# Define la función para mostrar los resultados del lanzamiento
def mostrar_resultados(dado1, dado2, puntaje):
    resultado_texto = font.render(f"Tirada: {dado1}, {dado2}. Puntuación: {puntaje}", True, WHITE)
    screen.blit(resultado_texto, (50, 150))

# Define la función principal del juego
def jugar():
    while True:
        # Maneja los eventos del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtiene la posición del cursor del mouse
                pos = pygame.mouse.get_pos()
                if 150 <= pos[0] <= 250 and 100 <= pos[1] <= 130:
                    # Lanza los dados y muestra los resultados
                    dados = lanzar_dados()
                    mostrar_resultados(*dados)
                elif 150 <= pos[0] <= 250 and 150 <= pos[1] <= 180:
                    # Sale del juego
                    pygame.quit()
                    quit()

        # Dibuja la pantalla
        screen.fill(BLACK)

        # Dibuja los botones
        pygame.draw.rect(screen, GREEN, [150, 100, 100, 30])
        pygame.draw.rect(screen, GREEN, [150, 150, 100, 30])

        # Agrega texto a los botones
        jugar_texto = font.render("Jugar", True, WHITE)
        salir_texto = small_font.render("Salir", True, WHITE)
        screen.blit(jugar_texto, (165, 105))
        screen.blit(salir_texto, (170, 155))

        # Actualiza la pantalla
        pygame.display.update()

# Ejecuta el juego
jugar()