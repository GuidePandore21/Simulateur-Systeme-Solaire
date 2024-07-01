import pygame
from SystemeSolaire import SystemeSolaire
from CorpsCeleste import CorpsCeleste

WIDTH = 600
HEIGHT = 600

systemeSolaire = SystemeSolaire()

Soleil = CorpsCeleste("Soleil", 0, 0, 0, 0, 696340000 * 30, 1.989e30, (255, 223, 0))
systemeSolaire.ajouterCorpsCeleste(Soleil)

Mercure = CorpsCeleste("Mercure", 0.387 * CorpsCeleste.UA, 0, 0, 47362, 2439700 * 750, 3.3011e23, (169, 169, 169))
systemeSolaire.ajouterCorpsCeleste(Mercure)

Venus = CorpsCeleste("Vénus", 0.723 * CorpsCeleste.UA, 0, 0, 35025.71, 6051800 * 500, 4.8675e24, (255, 223, 196))
systemeSolaire.ajouterCorpsCeleste(Venus)

Terre = CorpsCeleste("Terre", CorpsCeleste.UA, 0, 0, 29783, 6371000 * 750, 5.972e24, (87, 138, 204))
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
