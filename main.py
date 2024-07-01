import pygame
from SystemeSolaire import SystemeSolaire
from CorpsCeleste import CorpsCeleste

WIDTH = 600
HEIGHT = 600

jaune = (255, 255, 0)
bleu = (150, 150, 255)
blanc = (255, 255, 255)

systemeSolaire = SystemeSolaire()

Soleil = CorpsCeleste("Soleil", 0, 0, 0, 0, 696340000 * 30, 1.989e30, jaune)
systemeSolaire.ajouterCorpsCeleste(Soleil)

Terre = CorpsCeleste("Terre", CorpsCeleste.UA, 0, 0, 29783, 6371000 * 500, 5.972e24, bleu)
systemeSolaire.ajouterCorpsCeleste(Terre)

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("black")
    
    for planet in systemeSolaire.listeCorpsCeleste:
        planet.calculPositionEtVitesse(systemeSolaire.listeCorpsCeleste)
        pygame.draw.circle(SCREEN, planet.couleur, (int(planet.x * CorpsCeleste.SCALE + WIDTH // 2), int(planet.y * CorpsCeleste.SCALE + HEIGHT // 2)), planet.rayon)
    
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
