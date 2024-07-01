import pygame
from math import radians
from SystemeSolaire import SystemeSolaire
from CorpsCeleste import CorpsCeleste

WIDTH = 1200
HEIGHT = 800

ECHELLE_SOLEIL = 50
ECHELLE_PLANETE_ROCHEUSE = 5000
ECHELLE_PLANETE_GAZEUSE = 500

def dessinerAnneaux(surface, x, y, rayon, couleurs):
    num_segments = len(couleurs)
    angle_per_segment = 360 / num_segments

    for i in range(num_segments):
        start_angle = radians(i * angle_per_segment)
        end_angle = radians((i + 1) * angle_per_segment)
        pygame.draw.arc(surface, couleurs[i], (x-rayon, y-rayon, 2*rayon, 2*rayon), start_angle, end_angle, 1)

systemeSolaire = SystemeSolaire()

Soleil = CorpsCeleste("Soleil", 0, 0, 0, 0, 696340000 * ECHELLE_SOLEIL, 1.989e30, (255, 223, 0))
systemeSolaire.ajouterCorpsCeleste(Soleil)

Mercure = CorpsCeleste("Mercure", 0.387 * CorpsCeleste.UA, 0, 0, 47362, 2439700 * ECHELLE_PLANETE_ROCHEUSE, 3.3011e23, (169, 169, 169))
systemeSolaire.ajouterCorpsCeleste(Mercure)

Venus = CorpsCeleste("Vénus", 0.723 * CorpsCeleste.UA, 0, 0, 35025.71, 6051800 * ECHELLE_PLANETE_ROCHEUSE, 4.8675e24, (255, 223, 196))
systemeSolaire.ajouterCorpsCeleste(Venus)

Terre = CorpsCeleste("Terre", CorpsCeleste.UA, 0, 0, 29783, 6371000 * ECHELLE_PLANETE_ROCHEUSE, 5.972e24, (87, 138, 204))
systemeSolaire.ajouterCorpsCeleste(Terre)

Mars = CorpsCeleste("Mars", 1.523 * CorpsCeleste.UA, 0, 0, 24080, 3396200 * ECHELLE_PLANETE_ROCHEUSE, 6.418e23, (188, 39, 50))
systemeSolaire.ajouterCorpsCeleste(Mars)

Jupiter = CorpsCeleste("Jupiter", 5.202 * CorpsCeleste.UA, 0, 0, 13058, 71492000 * ECHELLE_PLANETE_GAZEUSE, 1.898e27, (255, 145, 79))
systemeSolaire.ajouterCorpsCeleste(Jupiter)

Saturne = CorpsCeleste("Saturne", 9.536 * CorpsCeleste.UA, 0, 0, 9640, 60268000 * ECHELLE_PLANETE_GAZEUSE, 5.684e26, (242, 226, 191))
systemeSolaire.ajouterCorpsCeleste(Saturne)

Uranus = CorpsCeleste("Uranus", 19.189 * CorpsCeleste.UA, 0, 0, 6796, 25559000 * ECHELLE_PLANETE_GAZEUSE, 8.681e25, (173, 216, 230))
systemeSolaire.ajouterCorpsCeleste(Uranus)

Neptune = CorpsCeleste("Neptune", 30.069 * CorpsCeleste.UA, 0, 0, 5432, 24764000 * ECHELLE_PLANETE_GAZEUSE, 1.024e26, (72, 61, 139))
systemeSolaire.ajouterCorpsCeleste(Neptune)

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
        X = int(planet.x * CorpsCeleste.SCALE + WIDTH // 2)
        Y = int(planet.y * CorpsCeleste.SCALE + HEIGHT // 2)
        pygame.draw.circle(SCREEN, planet.couleur, (X, Y), planet.rayon)
        
        if planet.nom == "Saturne":
                for i, couleur in enumerate([(210, 180, 140)]):
                    dessinerAnneaux(SCREEN, X, Y, planet.rayon + (i + 1)*2, [couleur])
    
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
