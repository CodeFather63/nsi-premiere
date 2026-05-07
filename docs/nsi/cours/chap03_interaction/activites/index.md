# Contrôler la tortue ...

## OBJECTIFS

Dans l’activité du chapitre 2, nous avons créé une fonction `polygone` qui trace un polygone à l’aide de la bibliothèque `turtle`. Nous allons maintenant créer une interface graphique de la page 49, pour utiliser cette fonction en cliquant simplement sur un bouton.

## 🔘 Des boutons pour lancer des fonctions

Pour commencer, nous créons un bouton pour dessiner un polygone. Nous utilisons la fonction `button` de la bibliothèque [`nsi_ui`](nsi_ui.py), créée spécialement pour ce manuel. Elle prend pour paramètres le titre du bouton et la fonction Python à appeler lorsqu’on clique dessus.

```python
from turtle import *
from nsi_ui import *

# insérer ici la fonction polygone du chapitre 2

def creer_polygone():
    """ Fonction sans paramètres que l’on va associer au bouton """
    polygone(5, 60)

button("Polygone", creer_polygone)  # bouton pour faire le dessin
```