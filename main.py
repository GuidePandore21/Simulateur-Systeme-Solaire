import pygame
from SystemeSolaire import SystemeSolaire
from CorpsCeleste import CorpsCeleste

WIDTH = 500
HEIGHT = 500

jaune = (255, 255, 0)
bleu = (0, 0, 255)

systemeSolaire = SystemeSolaire()

Soleil = CorpsCeleste("Soleil", WIDTH//2, HEIGHT//2, 0, 0, 696340000, 1.989e30, jaune)
systemeSolaire.ajouterCorpsCeleste(Soleil)

Terre = CorpsCeleste("Terre", WIDTH//2 + CorpsCeleste.UA * CorpsCeleste.SCALE, HEIGHT//2, 0, 0, 6371000, 5.972e24)
systemeSolaire.ajouterCorpsCeleste(Terre)

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
