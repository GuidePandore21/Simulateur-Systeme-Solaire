class CorpsCeleste:
    G = 6.67430e-11  # Constante gravitationnelle
    AU = 1.496e11  # Unité astronomique en mètres
    SCALE = 250 / AU  # Échelle de l'affichage (250 pixels par unité astronomique)
    TIMESTEP = 3600 * 24  # Une journée en secondes
    
    def __init__(self, nom, x, y, rayon, masse, couleur):
        self.nom = nom
        self.x = x
        self.y = y
        self.rayon = rayon
        self.masse = masse
        self.couleur = couleur

