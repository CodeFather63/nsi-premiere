from turtle import *
from nsi_ui import *

def polygone(n, cote):
    """Tracer un polygone à n côtés de longueur cote"""
    for i in range(n):
        forward(cote)
        right(360 / n)

def creer_polygone():
    """Fonction associée au bouton Polygone"""
    polygone(5, 60)

def effacer_ecran():
    """Fonction associée au bouton Efface l'écran"""
    clear()

polygone(5, 60)

button("Polygone", creer_polygone)       # bouton pour faire le dessin
button("Efface l'écran", effacer_ecran)  # bouton pour effacer le dessin


