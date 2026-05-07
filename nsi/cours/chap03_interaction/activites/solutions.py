from turtle import *
from nsi_ui import *

def polygone(n, cote):
    """Tracer un polygone à n côtés de longueur cote"""
    for i in range(n):
        forward(cote)
        right(360 / n)


tirette_taille = slider("Taille",10,100)
tirette_nbcote = slider("Nb Coté",3,50)

def creer_polygone():
    """Fonction associée au bouton Polygone"""
    polygone(get_int(tirette_nbcote), get_int(tirette_taille))

def effacer_ecran():
    """Fonction associée au bouton Efface l'écran"""
    clear()

polygone(get_int(tirette_nbcote), get_int(tirette_taille))

button("Polygone", creer_polygone)       # bouton pour faire le dessin
button("Efface l'écran", effacer_ecran)  # bouton pour effacer le dessin

def gauche():
    left(10)
def droite():
    right(10)
def avance():
    forward(10)
    
onkey(droite, "Right")
onkey(gauche, "Left")
onkey(avance, "Up")  # paramètres : fonction à appeler, nom de la touche
