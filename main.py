import pygame

WIDTH = 500
HEIGHT = 500

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
RUNNING = True
DT = 0

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("green")
    
    pygame.display.flip()
    
    DT = CLOCK.tick(60) / 1000

pygame.quit()
