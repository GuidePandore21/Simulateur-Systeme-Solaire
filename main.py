import pygame
from SystemeSolaire import SystemeSolaire
from CorpsCeleste import CorpsCeleste

WIDTH = 600
HEIGHT = 600

ECHELLE_SOLEIL = 50
ECHELLE_PLANETE = 1000

systemeSolaire = SystemeSolaire()

Soleil = CorpsCeleste("Soleil", 0, 0, 0, 0, 696340000 * ECHELLE_SOLEIL, 1.989e30, (255, 223, 0))
systemeSolaire.ajouterCorpsCeleste(Soleil)

Mercure = CorpsCeleste("Mercure", 0.387 * CorpsCeleste.UA, 0, 0, 47362, 2439700 * ECHELLE_PLANETE, 3.3011e23, (169, 169, 169))
systemeSolaire.ajouterCorpsCeleste(Mercure)

Venus = CorpsCeleste("Vénus", 0.723 * CorpsCeleste.UA, 0, 0, 35025.71, 6051800 * ECHELLE_PLANETE, 4.8675e24, (255, 223, 196))
systemeSolaire.ajouterCorpsCeleste(Venus)

Terre = CorpsCeleste("Terre", CorpsCeleste.UA, 0, 0, 29783, 6371000 * ECHELLE_PLANETE, 5.972e24, (87, 138, 204))
systemeSolaire.ajouterCorpsCeleste(Terre)

Mars = CorpsCeleste("Mars", 1.523 * CorpsCeleste.UA, 0, 0, 24080, 3396200 * ECHELLE_PLANETE, 6.418e23, (188, 39, 50))
systemeSolaire.ajouterCorpsCeleste(Mars)

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
