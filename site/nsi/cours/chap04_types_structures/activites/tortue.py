# coding: utf-8

##### ##### #####   ##### ##### ##### 
#####     DESSINER AVEC LA TORTUE   ##
##### ##### #####   ##### ##### #####

###################################
#####                         #####
#####  1. AFFICHER UN DESSIN  #####
#####                         #####
###################################

from turtle import *
from nsi_ui import *

##### 1a. Fonction dessine de base #####

maison = [(0,0), (0,100), (50,150), (100,100), (100,0), (0,0)]

def dessine(points: list[tuple[int, int]]) -> None:
    # On se déplace sans dessiner au premier point
    penup()
    goto(points[0][0], points[0][1])
    pendown()
    # On trace les points suivants
    for x, y in points[1:]:
        goto(x, y)

##### test #####
#dessine(maison)

##### 1b. Autres dessins #####

sapin = [(0,0), (0,20), (-40,20), (0,80), (-30,80), (0,140), (30,80), (0,80), (40,20), (0,20), (0,0)]

etoile = [(0,0), (30,90), (60,0), (-20,55), (70,55), (0,0)]

##### test #####
#dessine(sapin)
#dessine(etoile)

##### 1c. Dessine à partir de la position actuelle de la tortue #####

def dessine(points: list[tuple[int, int]]) -> None:
    # On récupère la position initiale de la tortue
    origine_x: float = xcor()
    origine_y: float = ycor()
    # On se déplace sans dessiner au premier point décalé par la position initiale
    penup()
    goto(origine_x + points[0][0], origine_y + points[0][1])
    pendown()
    # On trace les points suivants en ajoutant la position initiale
    for x, y in points[1:]:
        goto(origine_x + x, origine_y + y)

##### test #####
#goto(100, 100)
#dessine(maison)

###################################
#####                         #####
##### 2. DESSIN A MAIN LEVEE  #####
#####                         #####
###################################

##### 2a. Dessiner en cliquant et déplaçant #####

def sauter(x: float, y: float) -> None:
    """ Déplace la tortue sans dessiner à la position x, y """
    penup()
    goto(x, y)
    pendown()

onscreenclick(sauter)  # bouger la tortue lorsqu'on clique dans la fenêtre

def tracer(x: float, y: float) -> None:
    """ Dessine un trait jusqu'à la position x, y """
    goto(x, y)

ondrag(tracer)  # dessiner lorsqu'on déplace la tortue avec la souris

##### test #####
#mainloop()

##### 2b. Enregistrer les points dans une variable globale #####

dessin: list[tuple[float, float]] = []

def sauter(x: float, y: float) -> None:
    """ Déplace la tortue sans dessiner, initialise le dessin """
    global dessin
    # On réinitialise le dessin quand on commence à dessiner
    dessin = []
    penup()
    goto(x, y)
    pendown()
    dessin.append((x, y))

onscreenclick(sauter)

def tracer(x: float, y: float) -> None:
    """ Dessine un trait et enregistre le point """
    goto(x, y)
    dessin.append((x, y))

ondrag(tracer)

##### test #####
#mainloop()

###################################
#####                         #####
##### 3. DESSINS NOMMES       #####
#####                         #####
###################################

dessin: list[tuple[float, float]] = []
dessins: dict[str, list[tuple[float, float]]] = {
    "maison": [(0,0), (0,100), (50,150), (100,100), (100,0), (0,0)],
}

def sauter(x: float, y: float) -> None:
    global dessin
    dessin = []
    penup()
    goto(x, y)
    pendown()
    dessin.append((x, y))

onscreenclick(sauter)

def tracer(x: float, y: float) -> None:
    goto(x, y)
    dessin.append((x, y))

ondrag(tracer)

def effacer() -> None:
    """ Efface l'écran """
    clear()

def enregistrer() -> None:
    """ Enregistre le dessin courant sous le nom saisi """
    nom: str = get_string(champ_nom)
    if nom != "":
        dessins[nom] = list(dessin)
        update_list(liste_dessins, dessins)

def dessiner_nom() -> None:
    """ Redessine le dessin portant le nom saisi s'il existe """
    nom: str = get_string(champ_nom)
    if nom in dessins:
        dessine(dessins[nom])

# Interface avec nsi_ui
begin_horizontal()
champ_nom = entry("Nom du dessin")
button("Enregistrer", enregistrer)
button("Dessiner", dessiner_nom)
button("Effacer", effacer)
end_horizontal()

liste_dessins = listbox("Dessins enregistrés", dessins, dessiner_nom)

start_ui()
