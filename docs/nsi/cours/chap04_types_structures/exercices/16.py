#
# Exercice 16 - Calcul de distances
#

# un dessin est un tableau de tuples (x, y)
dessin1 = [(100, 100), (200, 200), (200, 100), (100, 200), (100, 100)]
dessin2 = [(208, 64), (142, 23), (130, 82), (84, 98), (342, 150), (135, 81), 
           (145, 28), (156, 74), (237, 61), (348, 150), (156, 76)]
dessin3 = [(145, 25), (66, 34), (134, 53), (97, 57), (57, 48), (100, 43), 
           (174, 62), (130, 66), (0, 37), (141, 23), (140, 13), (247, 169), 
           (371, 184), (279, 45), (139, 12), (2, 35)]

# fonction pour afficher un dessin
from matplotlib.pyplot import plot, show
def affiche_dessin(dessin):
    plot([p[0] for p in dessin], [p[1] for p in dessin])
    show()

# afficher le premier dessin
affiche_dessin(dessin1)


# a) Écrire une fonction `distance` qui prend deux tuples contenant chacun 
# deux coordonnées *x, y*, et qui retourne leur distance euclidienne. 
# Pour rappel, la fonction `sqrt` retourne la racine carrée d’une expression, 
# et doit être importée depuis la bibliothèque `math`.


# b) Un dessin est stocké dans un tableau contenant ses points successifs 
# sous forme de tuples *(x, y)*. Écrire une fonction qui prend en paramètre 
# un tel tableau et retourne les dimensions *(largeur, hauteur)* du dessin.


# c) Écrire une fonction qui calcule la longueur du dessin, en utilisant 
# la fonction `distance` de la première question.

