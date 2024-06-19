from math import sqrt

class CorpsCeleste:
    G = 6.67430e-11  # Constante gravitationnelle
    UA = 1.496e11  # Unité astronomique en mètres (Distance Terre-Soleil)
    SCALE = 250 / UA  # Échelle de l'affichage (250 pixels par unité astronomique)
    TIMESTEP = 3600 * 24  # Une journée en secondes
    
    def __init__(self, nom, x, y, rayon, masse, couleur):
        self.nom = nom
        self.x = x
        self.y = y
        self.rayon = rayon
        self.masse = masse
        self.couleur = couleur

    def distanceAvecAutreCorpsCeleste(self, autreCorpsCeleste):
        return sqrt((self.x - autreCorpsCeleste.x)**2, (self.y - autreCorpsCeleste.y)**2) / self.SCALE

    def forceGravitationnel(self, autreCorpsCeleste):
        return self.G * self.masse * autreCorpsCeleste.masse / self.distanceAvecAutreCorpsCeleste(self, autreCorpsCeleste)**2