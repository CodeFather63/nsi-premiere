# Exercices Python — Tuples, Listes et Dictionnaires

## Exercice 1 — Points

On représente un point par un tuple *(x, y)* de ses coordonnées.

- Écrire une fonction `milieu` qui prend deux points `p1` et `p2` en paramètres et retourne le milieu du segment *(p1, p2)*.

---

## Exercice 2 — Dates

On représente une date par un tuple *(j, m, a)* où *j* est le jour du mois, *m* le numéro du mois (de 1 à 12) et *a* l'année.

a. Écrire une fonction `anterieur` qui prend deux dates `d1` et `d2` en paramètres et retourne `True` si `d1` est antérieure à `d2`.

b. Écrire une fonction `age` qui prend deux dates `d1` et `d2` en paramètres et retourne le nombre d'années pleines entre `d1` et `d2`. Peut-on utiliser la fonction de la question a. ?

---

## Exercice 3 — Personnes

On représente une personne par un tuple *(nom, date)* où *nom* est lui-même un tuple formé du prénom et du nom, et *date* est également un tuple représentant la date de naissance comme dans l'exercice 2.

Écrire une fonction qui prend une personne en paramètre et retourne un tuple formé du nom de famille et de l'année de naissance.

---

## Exercice 4 — Moyenne

Écrire une fonction `moyenne` qui prend en paramètre un tableau de nombres et retourne leur moyenne arithmétique.

---

## Exercice 5 — Tableau ordonné

Écrire une fonction `est_ordonne` qui prend en paramètre un tableau de nombres et retourne `True` si ses éléments sont ordonnés par ordre croissant.

---

## Exercice 6 — Zip et Unzip

On dispose d'un tableau `t = [(0,0), (0,100), (50,150), (100,100), (100,0)]` dont les éléments sont des tuples *(x, y)* représentant des points.

a. Écrire une fonction `unzip` qui prend un tel tableau `t` en paramètre et retourne un tuple *(tx, ty)* de deux tableaux contenant respectivement les coordonnées *x* et *y* des points de `t`.

b. Écrire une fonction `zip` qui réalise l'opération inverse : à partir de deux tableaux *tx* et *ty* de nombres, retourner un tableau de tuples *(x, y)*.

---

## Exercice 7 — Divisible par 7

a. Initialiser un tableau `divisible_7` de 1000 booléens de valeur `False`, puis écrire ensuite une boucle qui met à `True` les éléments du tableau dont l'indice est divisible par 7.

Par exemple, `divisible_7[2]` est `False` mais `divisible_7[14]` est `True`.

b. Combien de nombres inférieurs à 1 000 sont divisibles par 7 ? Quel est le plus grand nombre divisible par 7 et inférieur à 1 000 ?

---

## Exercice 8 — Palindrome

Écrire une fonction `palindrome` qui prend en paramètre une chaîne de caractères et retourne `True` si c'est un palindrome, c'est-à-dire s'il peut se lire dans les deux sens, comme le mot « ressasser ».

---

## Exercice 9 — Entier depuis une chaîne

Écrire une fonction qui prend en paramètre une chaîne de caractères représentant un entier positif, par exemple `"12345"`, et retourne le nombre entier correspondant, sans utiliser la fonction `int()`.

---

## Exercice 10 — Mot de passe

Écrire une fonction qui prend en paramètre un mot de passe et retourne `True` s'il vérifie les propriétés suivantes : il a au moins 8 caractères et contient au moins une majuscule, une minuscule, un chiffre et un caractère spécial (qui n'est ni une lettre ni un chiffre).

---

## Exercice 11 — Nombre de mots

Écrire deux versions d'une fonction `nb_mots` qui prend en paramètre une chaîne de caractères et retourne le nombre de mots dans la phrase. On suppose que tous les mots sont séparés par un espace. Ainsi, `nb_mots("Le petit chat est mort")` retourne 5.

- Une version doit utiliser la méthode `split` des chaînes de caractères.
- L'autre non.

---

## Exercice 12 — Longueur des mots

Écrire deux versions d'une fonction `longueur_mots` qui prend en paramètre une phrase (une chaîne de caractères) et retourne un tableau contenant la longueur des mots qui la composent. Ainsi, `longueur_mots("Le petit chat est mort")` retourne `[2, 5, 4, 3, 4]`.

- Une version doit utiliser la méthode `split` des chaînes de caractères.
- L'autre non.

---

## Exercice 13 — Capitales

Initialiser un dictionnaire `capitales` qui associe à chaque nom de pays le nom de sa capitale avec quelques pays européens. Écrire une fonction qui prend un nom de ville en paramètre et retourne le pays dont elle est la capitale, ou `None` si elle n'est pas dans le dictionnaire.

---

## Exercice 14 — Personnes (dictionnaire)

On considère un dictionnaire `personnes` qui associe à des noms de personnes un dictionnaire contenant des informations personnelles :

```python
personnes = {
    "Jean Aymar": {"taille": 178, "pays": "USA", "age": 31},
    "Clio Patre": {"pays": "Portugal", "age": 32, "taille": 179}
}
```

a. Écrire une fonction qui prend un nom de personne en paramètre et retourne son age, ou `None` si la personne n'est pas dans le dictionnaire.

b. Écrire une fonction qui calcule la taille moyenne des personnes dans le dictionnaire.

---

## Exercice 15 — Cartes à jouer

On définit une carte comme un tuple *(valeur, couleur)*. *valeur* est un entier de 2 à 14 inclus, où 11 représente le Valet et 14 l'As. *couleur* est une chaîne de caractères parmi « Pique », « Coeur », « Carreau », « Trèfle ».

a. Écrire une fonction `carte_valide` qui prend un tuple en paramètre et retourne un booléen qui indique s'il représente une carte valide.

b. Écrire une fonction `nom_carte` qui prend un tuple représentant une carte en paramètre et retourne une chaîne de caractères avec le nom de la carte, par exemple `"As de Trèfle"` ou `"7 de Pique"`.

c. Écrire un programme qui crée un tableau contenant toutes les cartes d'un jeu de 52 cartes.

d. À l'aide de la fonction `random()` de la bibliothèque `random`, tirer une carte au hasard dans le tableau et afficher son nom.

---

## Exercice 16 — Calcul de distances

[Télécharger le script de départ](16.py)

a. Écrire une fonction `distance` qui prend deux tuples contenant chacun des coordonnées *x, y*, et qui retourne leur distance euclidienne. Pour rappel, la fonction `sqrt` retourne la racine carrée d'une expression, et doit être importée depuis la bibliothèque `math`.

b. Un dessin est stocké dans un tableau contenant ses points successifs sous forme de tuples *(x, y)*. Écrire une fonction qui prend en paramètre un tel tableau et retourne les dimensions *(largeur, hauteur)* du dessin.

c. Écrire une fonction qui calcule la longueur du dessin, en utilisant la fonction `distance` de la première question.

---

## Exercice 17 — Inverser un tableau

a. Écrire une fonction `inverse_tableau` qui prend en paramètre un tableau et retourne un tableau avec les mêmes éléments en ordre inverse.

b. Écrire une fonction `inverse_chaine` qui fait la même chose pour une chaîne de caractères. Peut-on utiliser la fonction `inverse_tableau` ?

---

## Exercice 18 — Tester le hasard

La fonction `random` de la bibliothèque Python `random` retourne des nombres aléatoires entre 0 et 1. On veut vérifier que ces nombres sont bien aléatoires, c'est-à-dire qu'ils sont uniformément répartis entre 0 et 1.

a. Écrire un programme qui appelle `random` 1 000 fois et enregistre dans un tableau `t` de dix entiers le nombre de fois où le résultat est dans chacun des dix intervalles [0, 0.1[, [0.1, 0.2[, … [0.9, 1.0[. Afficher le résultat sous forme d'histogramme avec le code suivant :

```python
from matplotlib.pyplot import bar, show
bar(range(len(t)), t)
show()
```

b. Répéter le calcul et l'affichage plusieurs fois, avec un nombre de répétitions de plus en plus grand (jusqu'à 10 millions). Qu'observe-t-on ?

---

## Exercice 19 — Loi Normale

> **Note :** La fonction `randint(a, b)` de la bibliothèque `random` retourne un nombre aléatoire entre *a* et *b* inclus.

a. Simuler le lancement de deux dés et compter le nombre de fois où la somme vaut 1, 2, …, 12. Afficher l'histogramme comme dans l'exercice 18 pour différents (grands) nombres de tirages.

b. Modifier le programme précédent pour simuler le lancement de *n* dés un grand nombre de fois et afficher l'histogramme correspondant.

La courbe obtenue lorsque *n* augmente s'approche de la « Loi Normale » et est très utilisée en probabilités et statistiques.

c. Une autre façon de faire apparaître la Loi Normale est de simuler un jeu de pile ou face : tirer des séries de 100 lancers de pile ou face et compter le nombre de fois où pile apparaît. Compter dans chaque élément `t[i]` d'un tableau le nombre de fois où une série donne *i* fois pile. Afficher l'histogramme correspondant.

---

## Exercice 20 — Taux d'imposition

En France comme dans beaucoup de pays, les impôts et taxes suivent un barème progressif, appelé « tranches ». Ainsi le taux d'imposition sur le revenu est de 0 % en-dessous de 10 000 €, de 11 % entre 10 000 € et 25 000 €, de 30 % entre 25 000 et 75 000 €, 41 % entre 75 000 et 150 000 €, 45 % au-delà de 150 000 €.

a. Définir un type construit pour représenter les tranches d'imposition et initialiser une variable `tranches` avec les tranches définies ci-dessus.

b. Écrire une fonction qui calcule le montant de l'impôt étant donné un revenu.

c. Pour montrer la progressivité de l'impôt, créer à l'aide de cette fonction un tableau contenant les montants des impôts pour des revenus de 0 à 200 000 € par pas de 5 000 €. Afficher ce tableau à l'aide du code suivant, où `tx` est le tableau des abscisses (les revenus) et `ty` celui des ordonnées (l'impôt) :

```python
from matplotlib.pyplot import plot, show
plot(tx, ty)
show()
```

d. Même question mais cette fois afficher le *taux marginal d'imposition*, c'est-à-dire le rapport, exprimé en pourcentage, du montant de l'impôt par rapport au revenu.

e. Comparer le taux marginal avec le taux d'imposition de la tranche correspondante pour des revenus annuels de 15 000 €, 50 000 €, 200 000 €.

---

## Exercice 21 — Anagramme

a. Écrire une fonction `retire_element(t, e)` qui retire l'élément `e` de `t` s'il est présent et retourne `True`, ou sinon retourne `False`. On utilisera la méthode `pop` pour retirer l'élément du tableau.

b. Écrire une fonction `meme_contenu` qui prend en paramètres deux tableaux et retourne `True` s'ils contiennent les mêmes éléments, même si leur ordre diffère ; `False` sinon. Attention aux alias !

c. Utiliser cette fonction pour écrire une fonction `anagramme` qui prend en paramètres deux chaînes de caractères, et retourne `True` si elles sont composées des mêmes lettres dans un ordre différent.

---

## Exercice 22 — Mélanger un tableau

a. Écrire une fonction `mélanger` qui prend un tableau en paramètre et retourne un tableau avec les mêmes éléments dans un ordre aléatoire. On utilisera la méthode `pop` des tableaux et la fonction `randint` de la bibliothèque `random`. Attention aux alias !

b. Appliquer cette fonction au tableau des 52 cartes de l'exercice 15.

---

## Exercice 23 — Bataille

Dans le jeu de la Bataille, à chaque tour de jeu, chaque joueur pose une carte sur la table puis on établit celle qui l'emporte : un 3 bat un 2, un Valet bat un 10, un As bat un Roi.

a. Écrire une fonction `duel` qui prend deux tuples représentant deux cartes en paramètre et retourne 0 en cas d'égalité, 1 si la première carte gagne, 2 si c'est la seconde.

b. Écrire une fonction `tirer` qui tire une carte au hasard. À l'aide de cette fonction, écrire une fonction `jouer` qui tire deux cartes et les met en duel. En cas d'égalité, elle tire deux nouvelles cartes jusqu'à ce qu'un joueur gagne. La fonction retourne un tuple formé du numéro du gagnant et du nombre de duels.

c. Modifier la fonction `tirer` pour utiliser la fonction `mélanger` de l'exercice précédent et ainsi éviter que l'on tire plusieurs fois la même carte.

---

## Exercice 24 — Inverser un dictionnaire

a. Écrire une fonction `inverse_dict` qui prend en paramètre un dictionnaire et inverse ses clés et ses valeurs. Appliquer cette fonction au dictionnaire des capitales de l'exercice 13.

b. Est-il toujours possible d'inverser un dictionnaire ? Pourquoi ?

c. Est-on sûr que `inverse_dict(inverse_dict(dico)) == dico` ? Pourquoi ?

---

## Exercice 25 — Scrabble

Le jeu du Scrabble consiste à construire des mots à l'aide de lettres sur une grille. Chaque lettre a une valeur numérique permettant de calculer des scores.

Le dictionnaire suivant indique les valeurs des lettres dans les règles françaises du Scrabble :

```python
valeurs_Scrabble = {10: 'kwxyz', 8: 'jq', 4: 'fhv', 3: 'bcp', 2: 'dmg'}
```

Toutes les autres lettres ont une valeur de 1.

a. En utilisant `valeurs_Scrabble`, calculer la valeur des mots « pizza », « whisky », « dédramatiser » (é compte pour e).

b. Il n'est pas pratique de parcourir chaque valeur et chaque chaîne de `valeurs_Scrabble` pour trouver la valeur de chaque lettre. À partir de `valeurs_Scrabble`, créer le dictionnaire `lettres_Scrabble` qui fait correspondre à chaque lettre de l'alphabet son score : `{"a": 1, "b": 3, "c": 3, …}`.

c. Écrire une fonction qui calcule la valeur d'un mot. Quel mot apporte le plus de points parmi : entrais, ratines, satiner, riantes, transie ?

d. J'ai accès à une case « lettre compte triple » au 4è élément d'une rangée de 7 lettres. Cette case triple la valeur des points de la lettre qui est posée dessus. Écrire un programme permettant de savoir lequel des mots précédents me rapportera le plus de points.

---

## Exercice 26 — Géographie

[Télécharger le script de départ](26.py)

a. On dispose d'un dictionnaire `villes_coordonnees` qui associe à chaque nom de ville (chaîne) ses coordonnées sous la forme d'un tuple *(longitude, latitude)*. Afficher les noms de toutes les villes dont la latitude est inférieure à 23,43 degrés.

b. On dispose également d'un dictionnaire `villes_population` qui associe à chaque nom de ville (chaîne) son nombre d'habitants (entier). Afficher les coordonnées de la ville ayant le plus d'habitants.

c. On dispose enfin d'un dictionnaire `villes_pays` qui associe à chaque nom de pays (chaîne) un tableau de ses villes. Afficher le nombre total d'habitants des villes d'un pays donné et la latitude et la longitude moyenne de ces villes.

---

## Exercice 27 — Liste de tâches simple

On définit une liste de tâches `todo_list` sous la forme d'un dictionnaire dont les clés sont des chaînes de caractères (les tâches à effectuer) et les valeurs des booléens (selon qu'une tâche est effectuée ou non).

a. Créer un dictionnaire `todo_list` et y ajouter les tâches « Faire les courses » (fait), « Ranger le garage » (à faire), et « Compléter l'exercice 4 » (à faire).

b. Écrire une fonction qui retourne le nombre de tâches non complétées dans `todo_list`, et les affiche.

c. Écrire un programme avec une interface textuelle pour gérer la liste de tâches. L'interface affiche la liste numérotée des tâches et attend une commande de l'utilisateur. Les tâches déjà réalisées sont précédées d'un caractère `v`. Les commandes sont :

- `+` pour ajouter une tâche. Le programme demande ensuite le nom de la tâche ;
- `-` suivi d'un numéro pour retirer la tâche correspondante ;
- `v` suivi d'un numéro pour changer le statut fait / à faire de la tâche correspondante ;
- `?` pour afficher seulement les tâches restant à faire.

---

## Exercice 28 — Annuaire

a. Écrire une fonction qui prend en paramètre une chaîne de caractères formée d'un prénom, d'un nom et d'un numéro de téléphone, par exemple `"Jean Dupont 0987654321"` et retourne un tuple constitué du nom, du prénom et du numéro de téléphone.

b. On veut créer un dictionnaire dont les clés sont des noms de personne et les valeurs des chaînes de caractères représentant leur numéro de téléphone. Écrire une fonction qui prend un tuple de la forme ci-dessus et ajoute l'information au dictionnaire.

c. Écrire un programme avec une interface textuelle pour gérer un annuaire. Le programme demande si l'on veut ajouter ou rechercher une entrée dans l'annuaire. Dans le premier cas, le programme demande à entrer sur une seule ligne le prénom, le nom et le numéro de téléphone et ajoute l'entrée au dictionnaire ; dans le second cas, il demande à entrer seulement le prénom et le nom et affiche le numéro de téléphone correspondant s'il existe, un message d'erreur sinon.

d. Modifier le contenu du dictionnaire et le programme pour que l'on puisse rechercher un numéro de téléphone en entrant seulement le nom ou le prénom.
