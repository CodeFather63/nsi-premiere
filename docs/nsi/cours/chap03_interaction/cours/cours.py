
# Chapitre 3 - Un peu d'interaction
# =================================
# 
# 1 Interaction textuelle
# ---------------------
# 
# ### 1.1 Afficher du texte

a = 3
b = 5.4
print("La somme de", a, "et", b, "est égale à", a+b)

#---

print(f"La somme de {a} et {b} est égale à {a+b}.")

# ### 1.2 Lire du texte

# attendre que l'utilisateur entre les valeurs de a et b
a = input("Valeur de a ? ")
b = input("Valeur de b ? ")
# convertir a et b en flottants, et calculer la somme
print("Resultat = ", float(a) + float(b))

# ### 1.3 Gérer les erreurs dans les entrées : l’instruction `try`

a = input("Valeur de a ? ") # entrer toto
b = input("Valeur de b ? ") # entrer tutu
print("Resultat = ", float(a) + float(b))

#---

try:
    a = float( input("Valeur de a ? ") )
    print("Resultat = ", a)
except ValueError:
    print("Oups, a n'est pas un nombre.")

#---

ok = False
while not ok:       # tant que la saisie n'est pas correcte
    try:
        a = float( input("Valeur de a ? ") )
        ok = True       # saisie correcte
    except ValueError:  # saisie incorrecte
        print("Erreur de saisie ! Entrer une valeur flottante :")

# 2 Interaction graphique
# ---------------------

# Importer la bibliothèque nsi_ui créée pour ce manuel
from nsi_ui import *

# ### 2.1 Fonctions de rappel

def coucou():
    print("Coucou")
def repete(f):  # f est une fonction
    f()         # on appelle f ...
    f()         # ... deux fois

repete(coucou)  # affiche "Coucou" deux fois

#---

from nsi_turtle import * # pour importer la fonction clear

button("Effacer", clear) # appelle clear() lorsqu'on clique le bouton
start_ui()

# ### 2.2 Interacteurs de base

from nsi_ui import *

# champs de saisie de texte pour entrer les valeurs de a et b
champA = entry("Valeur de a")
champB = entry("Valeur de b")

def ajouter():
    """ Afficher la somme des valeurs des champs A et B """
    a = get_float(champA)   # valeur entrée dans le champ A
    b = get_float(champB)   # valeur entrée dans le champ B
    
    set_text(resultat, a+b) # afficher le resultat

button("Somme", ajouter) # bouton pour lancer le calcul
resultat = label("")     # zone d'affichage du résultat
start_ui()               # lancer l'interface (on peut aussi utiliser main_loop())

# ### 2.3 Mise en page d’interfaces : les conteneurs

from nsi_ui import *

def soustraire():
    """ Afficher la somme des valeurs des champs A et B """
    a = get_float(champA)   # valeur entrée dans le champ A
    b = get_float(champB)   # valeur entrée dans le champ B
    set_text(resultat, a-b) # afficher le resultat

begin_vertical()   # début d'un conteneur vertical (vert)

begin_horizontal() # conteneur horizontal pour a et b (rouge)
champA = slider("Valeur de a", 0, 100)
champB = slider("Valeur de b", 0, 100)
end_horizontal()   # fin du premier conteneur horizontal

begin_horizontal() # 2e conteneur horizontal pour les boutons (bleu)
button("Somme", ajouter)
button("Différence", soustraire)
end_horizontal()   # fin du 2e conteneur horizontal

resultat = label("resultat")
end_vertical()     # fin du conteneur vertical

start_ui()

# ### 2.4 Les écouteurs d’événements
# 
# **Note :** Les deux programmes suivants ne fonctionnent pas dans Jupyter car 
# la bibliothèque `nsi_turtle` ne gère pas les événements dans cet environnement. 
# On peut les exécuter depuis Python en exécutant le programme `evenements.py`.

from nsi_turtle import *

# définir les fonctions de rappel
def actionXY(x, y):
    print(f'x = {x}, y = {y}')

def action():
    print('action!')

# actionXY est une fonction de rappel à deux paramètres, x et y
onclick(actionXY)         # clic sur la tortue
onscreenclick(actionXY)   # clic ailleurs sur l'écran
ondrag(actionXY)          # glissé sur la tortue

# action est une fonction de rappel sans paramètre
# t est un code de touche : lettre ('a', ...) ou nom ('Space', ...)
# onkey(action, t)
onkey(action, 't')         # appui sur la touche t
onkey(action, 'space')     # appui sur la touche espace

#---

from nsi_turtle import *

def avance():
    forward(10)

onkey(avance, 'a')  # taper "a" fait avancer la souris
ondrag(goto)        # cliquer-tirer la tortue lui fait suivre la souris
'''
