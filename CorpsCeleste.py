from math import sqrt, atan2, cos, sin

class CorpsCeleste:
    G = 6.67430e-11  # Constante gravitationnelle
    UA = 1.496e11  # Unité astronomique en mètres (Distance Terre-Soleil)
    SCALE = 250 / UA  # Échelle de l'affichage (250 pixels par unité astronomique)
    TIMESTEP = 3600 * 24  # Une journée en secondes
    
    def __init__(self, nom, x, y, vitesseX, vitesseY, rayon, masse, couleur):
        self.nom = nom
        self.x = x
        self.y = y
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.rayon = int(rayon * self.SCALE)
        self.masse = masse
        self.couleur = couleur

    def distanceAvecAutreCorpsCeleste(self, autreCorpsCeleste):
        return sqrt((self.x - autreCorpsCeleste.x)**2 + (self.y - autreCorpsCeleste.y)**2)
    
    def forceGravitationnelle(self, autreCorpsCeleste):
        distance = self.distanceAvecAutreCorpsCeleste(autreCorpsCeleste)
        force = self.G * self.masse * autreCorpsCeleste.masse / distance**2
        theta = atan2(autreCorpsCeleste.y - self.y, autreCorpsCeleste.x - self.x)
        forceX = cos(theta) * force
        forceY = sin(theta) * force
        return forceX, forceY
    
    def calculPositionEtVitesse(self, autresCorpsCelestes):
        totaleForceX = 0
        totaleForceY = 0
        
        for autreCorpsCeleste in autresCorpsCelestes:
            if autreCorpsCeleste != self:
                forceX, forceY = self.forceGravitationnelle(autreCorpsCeleste)
                totaleForceX += forceX
                totaleForceY += forceY
        
        # Calcul des accélérations : m/s²
        accelerationX = totaleForceX / self.masse
        accelerationY = totaleForceY / self.masse
        
        # Mise à jour des vitesses : m/s
        self.vitesseX += accelerationX * self.TIMESTEP
        self.vitesseY += accelerationY * self.TIMESTEP
        
        # Mise à jour des positions : px
        self.x += self.vitesseX * self.TIMESTEP
        self.y += self.vitesseY * self.TIMESTEP