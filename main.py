import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('My first pygame programme')

font = pygame.font.SysFont('comicsans', 32)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
x, y = 170, 200
a, b = 50, 100
direct_x = 1
direct_y = 1
direct_a = 1
direct_b = 1
FPS = 60
clock = pygame.time.Clock()
learningC = font.render("Learn C#", 1, RED, GREEN)
learningPython = font.render("Learn Python", 1, GREEN, BLUE)
width_P, height_P = learningPython.get_size()
width_C, height_C = learningC.get_size()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(learningC, (a, b))
    screen.blit(learningPython, (x, y))

    a += direct_a
    b += direct_b
    if a + width_C >= 600 or a < 0:
        direct_a = -direct_a
    if b + height_C >= 400 or b < 0:
        direct_b = -direct_b

    x += direct_x
    y += direct_y
    if x + width_P >= 600 or x < 0:
        direct_x = -direct_x
    if y + height_P >= 400 or y < 0:
        direct_y = -direct_y
    pygame.display.update()
