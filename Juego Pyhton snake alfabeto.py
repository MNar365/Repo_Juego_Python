import pygame
import sys
import random
import time

# Inicialización de pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
MORADO = (128, 0, 128)
NEGRO = (0, 0, 0)

# Dimensiones de pantalla
ANCHO = 640
ALTO = 480
TAM_CELDA = 20

# Direcciones
IZQUIERDA = (-1, 0)
DERECHA = (1, 0)
ARRIBA = (0, -1)
ABAJO = (0, 1)

font = None
all_positions = []
for row in range(0, (ANCHO // TAM_CELDA)):
    for col in range(0, (ALTO // TAM_CELDA)):
        all_positions.append((row, col))


class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = DERECHA

    def move(self):
        head = self.body[0]
        new_x, new_y = head[0] + self.direction[0], head[1] + self.direction[1]
        self.body = [(new_x, new_y)] + self.body[:-1]

    def grow(self):
        head = self.body[0]
        new_x, new_y = head[0] + self.direction[0], head[1] + self.direction[1]
        self.body = [(new_x, new_y)] + self.body

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, MORADO, (segment[0] * TAM_CELDA, segment[1] * TAM_CELDA, TAM_CELDA, TAM_CELDA))


screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Snake ABC')
clock = pygame.time.Clock()
snake = Snake()

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter_pos = (random.randint(0, (ANCHO // TAM_CELDA) - 1), random.randint(0, (ALTO // TAM_CELDA) - 1))
current_letter = 0
next_level = False

wrong_letters = letters.copy()
del wrong_letters[current_letter]
wrong_sample = random.sample(wrong_letters, 2)


def get_letter_positions():
    return random.sample(all_positions, 3)


letter_positions = get_letter_positions()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win_surface = font.render("Cerraste el juego", True, MORADO)
            rect = win_surface.get_rect(center=(ANCHO / 2, ALTO / 2))
            screen.blit(win_surface, rect)
            pygame.display.update()
            time.sleep(1)
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != DERECHA:
                snake.direction = IZQUIERDA
            if event.key == pygame.K_RIGHT and snake.direction != IZQUIERDA:
                snake.direction = DERECHA
            if event.key == pygame.K_UP and snake.direction != ABAJO:
                snake.direction = ARRIBA
            if event.key == pygame.K_DOWN and snake.direction != ARRIBA:
                snake.direction = ABAJO

    snake.move()

    # Verificar colisión con la letra
    if snake.body[0] in letter_positions:
        if snake.body[0] != letter_positions[0]:
            win_surface = font.render("Perdiste", True, MORADO)
            rect = win_surface.get_rect(center=(ANCHO / 2, ALTO / 2))
            screen.blit(win_surface, rect)
            pygame.display.update()
            time.sleep(1)
            break

        next_level = True

        snake.grow()
        current_letter += 1
        if current_letter >= len(letters):
            screen.fill(NEGRO)
            font = pygame.font.SysFont('arial', 36)
            win_surface = font.render("Ganaste", True, BLANCO)
            rect = win_surface.get_rect(center=(ANCHO / 2, ALTO / 2))
            screen.blit(win_surface, rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
        letter_positions = get_letter_positions()

    # Verificar colisión con bordes
    if (snake.body[0][0] < 0 or snake.body[0][1] < 0 or
            snake.body[0][0] >= ANCHO // TAM_CELDA or snake.body[0][1] >= ALTO // TAM_CELDA):
        win_surface = font.render("Perdiste", True, MORADO)
        rect = win_surface.get_rect(center=(ANCHO / 2, ALTO / 2))
        screen.blit(win_surface, rect)
        pygame.display.update()
        time.sleep(1)
        break

    # Verificar colisión con sí misma
    if snake.body[0] in snake.body[1:]:
        break

    screen.fill(BLANCO)

    # Dibujar letra
    font = pygame.font.SysFont('arial', 24)

    if next_level:
        next_level = False
        wrong_letters = letters.copy()
        del wrong_letters[current_letter]
        wrong_sample = random.sample(wrong_letters, 2)
    
    for i in range(3):
        if i == 0:
            letter = letters[current_letter]
        else:
            letter = wrong_sample[i - 1]
        letter_surface = font.render(letter, True, MORADO)
        screen.blit(letter_surface, (letter_positions[i][0] * TAM_CELDA, letter_positions[i][1] * TAM_CELDA))

    snake.draw(screen)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
